import os
import requests
from server import app, db
import server.models as models
from server.utils.pokeAPI import (parse_argument, set_types, set_stats,
  set_abilities, set_description_generation, write_file)


def pre_populate_pokemons(continue_from_last=False):
  """
  This function will fetch Pokémon data from PokéAPI(https://pokeapi.co/),
  including their abilities, adding to the database if needed and otherwise
  linking them to each Pokémon. It is necessary to execute the fuctions
  'pre_populate_types' and 'pre_populate_gens' contained within this file,
  otherwise an exception error will be raised.

  This function can only fetch 19 Pokémons at a time. This is due to limitations
  to the number of API requests from PókeAPI. URL offsets returned in PokéAPI
  responses are stored on a temporary 'last_pokeapi_request.txt' file. This file
  can be used to fetch new Pokémon, continuing from the previous request.
  
  *args:
  - continue_from_last (default: False)
  If 'True', sets up the request based on the data in 'last_pokeapi_request.txt'.
  Also ensures minimum amount of time between requests has elapsed. If 'False',
  fetches initial data using the provided base URL. Note that these will override
  data on 'last_pokeapi_request.txt', if any. Also note that no Pokémons will be
  added if this functions has been previously executed with its default argument,
  and also time between requests must be elapsed before reattempting.
  """
  # Retrieve base URL using helper function
  base_url = parse_argument.run(continue_from_last)
  print(f"\n\nFetching Pokémon list base URL: '{base_url}'.")

  # Request Pokémons to PokéAPI and retrieve response data
  r = requests.get(base_url)
  response_data = r.json()
  next_url = response_data["next"]
  previous_url = response_data["previous"]
  print(f"Success. Previous URL: '{previous_url}'. Next URL: '{next_url}'.\n\n")

  try:
    pokemon_urls = []
    # Get Pokémon URLs from response data
    for address in response_data["results"]:
      pokemon_urls.append(address["url"])

    # Iterate and request Pokémon URLs
    for url in pokemon_urls:
      print(f"Fetching Pokémon at '{url}'...\n\n")
      r = requests.get(url)
      response_data = r.json()

      # Retrieve readily available Pokémon data
      name = response_data["name"]
      print(f"Name: '{name}'.")
      height = response_data["height"]
      print(f"Height: '{height}'.")
      weight = response_data["weight"]
      print(f"Weight: '{weight}'.")

      # Set Pokémon types using helper function
      all_types = [poke_type["type"]["name"] for poke_type in response_data["types"]]
      types = set_types.run(all_types)
      print(f"Types: '{types}'.\n\n")

      # Set Pokémon base stats using helper function
      all_stats = [stat for stat in response_data["stats"]]
      base_stats = set_stats.run(all_stats)
      print("Exited 'set_stats' function.")
      base_hp = base_stats["base_hp"]
      base_attack = base_stats["base_attack"]
      base_defense = base_stats["base_defense"]
      base_speed = base_stats["base_speed"]
      base_sp_atk = base_stats["base_sp_atk"]
      base_sp_def = base_stats["base_sp_def"]
      print("Stats set.\n\n")

      # Set Pokémon abilities using helper function
      all_ability_urls = [ability["ability"]["url"] for ability in response_data["abilities"]]
      print(f"Got ability URLs:'{all_ability_urls}'.")
      abilities = set_abilities.run(all_ability_urls)
      print(f"Exited 'set_abilities' with: {abilities}'\n\n.")

      # Retrieve Pokémon description and generation using helper function
      # Also set the timing of the last request to PokéAPI
      species_url = response_data["species"]["url"]
      print(f"Species URL:'{species_url}'.")
      request_time, generation, description = set_description_generation.run(species_url)
      print(f"Retrieved: '{request_time}', '{generation}', '{description}''.\n\n")

      # Instantiate new Pokémon
      new_pokemon = models.Pokemon(
        species = name,
        description = description,
        height = height,
        weight = weight,
        base_hp = base_hp,
        base_attack = base_attack, 
        base_defense = base_defense,
        base_speed = base_speed,
        base_sp_atk = base_sp_atk,
        base_sp_def = base_sp_def
      )
      print("New Pokémon instantiated.")
      
      # Add new Pokémon to database
      db.session.add(new_pokemon)
      db.session.commit()
      print("New Pokémon added to database.\n")

      print("Adding relationships...\n")

      # Add Pokémon-Types relationships through insertions into helper table
      print("Executing insertions into table 'helper_pokemon_type'.")
      for type_id in types:
        insert = models.helper_pokemon_type.insert().values(pokemon=new_pokemon.id,
          type=type_id)
        db.session.execute(insert)
      print("Data inserted into table 'helper_pokemon_type'.\n")

      # Add Pokémon-Abilities relationships through insertions into helper table
      print("Executing insertions into table 'helper_pokemon_ability'.")
      for ability_id in abilities:
        insert = models.helper_pokemon_ability.insert().values(pokemon=new_pokemon.id,
          ability=ability_id)
        db.session.execute(insert)
      print("Data inserted into table 'helper_pokemon_ability'.\n")

      # Add Pokémon-Generation relationships through insertions into helper table
      print("Executing insertions into table 'helper_pokemon_generation'.")
      for generation_id in generation:
        insert = models.helper_pokemon_generation.insert().values(pokemon=new_pokemon.id,
          generation=generation_id)
        db.session.execute(insert)
      print("Data inserted into table 'helper_pokemon_generation'.\n")

      # Commit insertions to database
      db.session.commit()
      print("Relationships added to new Pokémon.\n\n")

    # Write new last request data file using helper function
    write_file.run(request_time, next_url, previous_url)

    # Finished succesfully 
    return print("Success.")


  # Print raised Exception to terminal if any
  except Exception as e:
    return print(str(e))
