import requests
import server.models as models


def run(species_url):
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

  # Request Pokémon species data to PokéAPI
  r = requests.get(species_url)
  species_data = r.json()

  # Set last request timing
  request_time = r.headers["Date"]
  print(f"Got last request date: '{request_time}'.")

  # Retrieve Pokémon generation from response data and query from database
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
  return request_time, generation, description
