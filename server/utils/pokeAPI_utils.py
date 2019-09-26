import os
import requests
import server.models as models
from server import app, db
from datetime import datetime, timedelta


def pre_populate_pokemons(continue_from_last=False):
  """
  This function will fetch Pokémon data from PokéAPI(https://pokeapi.co/),
  including their abilities, adding to the database if needed and otherwise
  linking them to each Pokémon. It is necessary to execute the fuctions
  'pre_populate_types' and 'pre_populate_gens' contained within this file,
  otherwise an exception error will be raised.

  This function can only fetch 18 Pokémons at a time. This is due to limitations
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
  def set_types(all_types):
    """
    This helper function receives and iterates over a list of Pokémon type names
    retrieved from PokéAPI, for the current Pokémon instance. At each iteration
    the type is queried from the database, and its 'id' appended to a new list.
    The 'id' list are foreign keys to be added to each new Pokémon instance.
    """
    print("\n\nEntered 'all_types' funtion.")
    types = []
    for poke_type in all_types:
      queried_type = models.Types.query.filter_by(name=poke_type).first()
      types.append(queried_type.id)
    
    return types


  def set_stats(all_stats):
    """
    This helper function receives and iterates over a base stats object retrieved
    from PokéAPI, for the current Pokémon instance. At each iteration the stat
    name is checked for and set accordingly. A dict with the base stats is returned.
    """
    print("Entered 'all_stats' function.\n\n")
    base_stats = {}
    print("\nEntering base_stats loop.\n")
    for stat_data in all_stats:
      if stat_data["stat"]["name"] == "speed":
        base_stats["base_speed"] = stat_data["base_stat"]
        print("Got speed.")

      elif stat_data["stat"]["name"] == "special-defense":
        base_stats["base_sp_def"] = stat_data["base_stat"]
        print("Got special-defense.")

      elif stat_data["stat"]["name"] == "special-attack":
        base_stats["base_sp_atk"] = stat_data["base_stat"]
        print("Got special-attack.")

      elif stat_data["stat"]["name"] == "defense":
        base_stats["base_defense"] = stat_data["base_stat"]
        print("Got defense.")

      elif stat_data["stat"]["name"] == "attack":
        base_stats["base_attack"] = stat_data["base_stat"]
        print("Got attack.")

      else:
        base_stats["base_hp"] = stat_data["base_stat"]
        print("Got health points.")
    
    print(f"Returning:\n{base_stats}.")
    return base_stats


  def set_abilities(all_ability_urls):
    """
    This helper function receives and iterates over a list of ability URLs retrived
    from PokéAPI, for the current Pokémon instance. Each iteration will request and
    retrieve necessary data on the current Pokémon's abilities. This data is used
    to populate the Abilities table, quering each at a time and adding it if needed.
    Finally, the function returns a list of ability 'ids' to be set as foreign
    keys on the current Pokémon instance.
    """
    print("Called 'set_abilites' function...\n")
    abilities = []
    for url in all_ability_urls:
      print(f"Fetching: '{url}'.")
      r = requests.get(url)
      response_data = r.json()
      name = response_data["name"]
      print(f"Retrieved ability: '{name}'.")

      queried_ability = models.Abilities.query.filter_by(name=name).first()

      if queried_ability is None:
        new_ability = models.Abilities(name=name,
          description=response_data["effect_entries"][0]["effect"])
        
        db.session.add(new_ability)
        db.session.commit()
        abilities.append(new_ability.id)

        print("Added to db.\n")
      
      else:
        abilities.append(queried_ability.id)
        print("Already on db.\n")
    
    return abilities
  

  def set_description_generation(species_url):
    """
    Due to the current PokéAPI structure, an additional request is needed in
    order to retrieve the Pokémon descripton and generation. This function
    receives the needed URL, which can be retrieved from the response data
    for the current Pokémon. Because this function executes the last request
    in order to gather all necessary Pokémon data, it is also used to set the
    time of the last request. Values returned are the description, an array
    of generation foreign keys, and a datetime object of the last request to
    PokéAPI.
    """
    print("Entered 'set_description_generation' function.\n")
    r = requests.get(species_url)
    request_time = r.headers["Date"]
    print(f"Got last request date: '{request_time}'.")
    species_data = r.json()

    generation_name = species_data["generation"]["name"]
    print(f"Got generation: '{generation_name}'.")
    queried_gen = models.Generation.query.filter_by(name=generation_name).first()
    generation = [queried_gen.id]

    all_descriptions = species_data["flavor_text_entries"]
    print("Entering 'all_descriptions' loop.")
    for description_data in all_descriptions:
      if description_data["language"]["name"] == "en":
        description = description_data["flavor_text"]
        print(f"Got description: '{description}'.")
        break
    
    print("Broke loop.\n")
    return request_time, generation, description


  def parse_argument(continue_from_last):
    """
    Sets up initial request based on the argument passed on the main outer
    function.
    """
    if continue_from_last:
      filename = os.path.join(app.root_path, "utils", "temp", "last_pokeapi_request.txt")
      print(f"\n\nRetrieving URL from file at '{filename}'...")
      with open(filename, "r") as file:
        lines = file.read().splitlines()
        date_string = lines[0]
        base_url = lines[1]
        print(f"Last PokéAPI request was issued at: '{date_string}'.")
        print(f"Next URL: '{base_url}'.")

      python_time = datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S %Z")
      elapsed = datetime.utcnow() - python_time

      if elapsed.seconds > 60:
        return base_url
      else:
        raise Exception("Not enough time has passed between requests to PokéAPI.")

    else:
      return "https://pokeapi.co/api/v2/pokemon/?limit=18/"  


  base_url = parse_argument(continue_from_last)
  print(f"\n\nFetching Pokémon list base URL: '{base_url}'.")
  r = requests.get(base_url)
  response_data = r.json()
  next_url = response_data["next"]
  previous_url = response_data["previous"]
  print(f"Success. Previous URL: '{previous_url}'. Next URL: '{next_url}'.\n\n")

  try:
    pokemon_urls = []
    for address in response_data["results"]:
      pokemon_urls.append(address["url"])

    for url in pokemon_urls:
      print(f"Fetching Pokémon at '{url}'...\n\n")
      r = requests.get(url)
      response_data = r.json()

      name = response_data["name"]
      print(f"Name: '{name}'.")
      height = response_data["height"]
      print(f"Height: '{height}'.")
      weight = response_data["weight"]
      print(f"Weight: '{weight}'.")

      all_types = [poke_type["type"]["name"] for poke_type in response_data["types"]]
      types = set_types(all_types)
      print(f"Types: '{types}'.\n\n")

      all_stats = [stat for stat in response_data["stats"]]
      base_stats = set_stats(all_stats)
      print("Exited 'set_stats' function.")
      base_hp = base_stats["base_hp"]
      base_attack = base_stats["base_attack"]
      base_defense = base_stats["base_defense"]
      base_speed = base_stats["base_speed"]
      base_sp_atk = base_stats["base_sp_atk"]
      base_sp_def = base_stats["base_sp_def"]
      print("Stats set.\n\n")

      all_ability_urls = [ability["ability"]["url"] for ability in response_data["abilities"]]
      print(f"Got ability URLs:'{all_ability_urls}'.")
      abilities = set_abilities(all_ability_urls)
      print(f"Exited 'set_abilities' with: {abilities}'\n\n.")

      species_url = response_data["species"]["url"]
      print(f"Species URL:'{species_url}'.")
      request_time, generation, description = set_description_generation(species_url)
      print(f"Retrieved: '{request_time}', '{generation}', '{description}''.\n\n")

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
      
      db.session.add(new_pokemon)
      db.session.commit()
      print("New Pokémon added to database.\n")

      print("Adding relationships...\n")
      print("Executing insertion into table 'helper_pokemon_type'.")
      for type_id in types:
        insert = models.helper_pokemon_type.insert().values(pokemon=new_pokemon.id,
          type=type_id)
        db.session.execute(insert)
      print("Data inserted into table 'helper_pokemon_type'.\n")

      print("Executing insertion into table 'helper_pokemon_ability'.")
      for ability_id in abilities:
        insert = models.helper_pokemon_ability.insert().values(pokemon=new_pokemon.id,
          ability=ability_id)
        db.session.execute(insert)
      print("Data inserted into table 'helper_pokemon_ability'.\n")

      print("Executing insertion into table 'helper_pokemon_generation'.")
      for generation_id in generation:
        insert = models.helper_pokemon_generation.insert().values(pokemon=new_pokemon.id,
          generation=generation_id)
        db.session.execute(insert)
      print("Data inserted into table 'helper_pokemon_generation'.\n")

      db.session.commit()
      print("Relationships added to new Pokémon.\n\n")

    filename = os.path.join(app.root_path, "utils", "temp", "last_pokeapi_request.txt")
    request_time = r.headers["Date"]

    print(f"Removing previous 'last_pokeapi_request.txt' at '{filename}'...")
    if os.path.exists(filename):
      os.remove(filename)

    print("Writing new file...\n")
    with open(filename, "a+") as file:
      file.write(str(request_time) + "\n")
      file.write(str(next_url) + "\n")
      file.write(str(previous_url) + "\n")
    
    return ("Success.")


  except Exception as e:
    return print(str(e))
