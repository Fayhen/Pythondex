import os
from server import app


def run(request_time, next_url, previous_url):
  """
  This helper function will write an updated 'last_pokeapi_request.txt',
  provided it received the right arguments.
  
  *args:
  request_time: The time the last request to PokéAPI was issued.
  next_url: Next URL to be requested to PokéAPI for subsequent Pokémon data.
  previous_url: The last requested issued to PokéAPI for Pokémon data retrieval.

  """
  filename = os.path.join(app.root_path, "utils", "temp", "last_pokeapi_request.txt")

  print(f"Removing previous 'last_pokeapi_request.txt' at '{filename}'...")
  if os.path.exists(filename):
    os.remove(filename)

  print("Writing new file...\n")
  with open(filename, "a+") as file:
    file.write(str(request_time) + "\n")
    file.write(str(next_url) + "\n")
    file.write(str(previous_url) + "\n")
  
  return print("New file created.\n\n")
