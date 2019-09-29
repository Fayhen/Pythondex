import requests
import server.models as models
from server import db


def run(species_url, name):
  """
  Returns last request time and the current Pokémon's descripton, generation and
  evolution chain. Requires 'species_url' and the current Pokémon instance name.

  *args
  - 'species_url': URL provided on the response data on each Pokémon request to
  PokéAPI. This URL is requested and contains necessary info to set up the
  evolution chain, description and generation for the current Pokémon instance.
  This is also the last request made to PokéAPI per Pokémon, therefore is used to
  set the timing of the last PokéAPI request.

  - 'name': The name of the current Pokémon instance species. The name is provided
  on the response data for each Pokémon request to PokéAPI. It is used to update
  the evolution chain, on Pokémons found to be the previous evoluiton stage of the
  current Pokémon instance.
  """
  print("Entered 'set_desc_gen_evolution' function.\n")

  # Request Pokémon species data to PokéAPI
  r = requests.get(species_url)
  species_data = r.json()

  # Set last request timing
  request_time = r.headers["Date"]
  print(f"Got last request date: '{request_time}'.")

  # Retrieve evolution data and updates chain on preexisting Pokémon, if necessary
  if species_data["evolves_from_species"] != None:
    evolves_from = species_data["evolves_from_species"]["name"]  
    print(f"Found previous evolutionary stage: '{evolves_from}'.")
    print(f"Updating evolution chain...")
    previous_stage = models.Pokemon.query.filter_by(species=evolves_from).first()
    previous_stage.evolves_into = name
    db.session.commit()
    print("Update successful.\n")
  else:
    evolves_from = None

  # Retrieve Pokémon generation and query from database
  generation_name = species_data["generation"]["name"]
  print(f"Got generation: '{generation_name}'.")
  queried_gen = models.Generation.query.filter_by(name=generation_name).first()
  generation = [queried_gen.id]

  # Iterate for Pokémon description in English on response data
  all_descriptions = species_data["flavor_text_entries"]
  print("Entering 'all_descriptions' loop.")
  for description_data in all_descriptions:
    if description_data["language"]["name"] == "en":
      description = description_data["flavor_text"]
      print(f"Got description: '{description}'.")
      break
  
  print("Broke loop.\n")

  # Return relevant data to main function
  return request_time, generation, description, evolves_from
