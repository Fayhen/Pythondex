import os
from server import app


def run(request_time, next_url, previous_url):
  """
  This helper function will write an updated 'last_pokeapi_request.txt' file,
  provided it receives the correct arguments.
  
  *args:
  request_time: The time the last request to PokéAPI was issued.
  next_url: Next URL to be requested to PokéAPI for subsequent Pokémon data.
  previous_url: The last requested issued to PokéAPI for Pokémon data retrieval.

  """
  # Ensure path exists
  filepath = os.path.join(app.root_path, "utils", "temp")
  if not os.path.exists(filepath):
    os.makedirs(filepath)
  
  filename = os.path.join(filepath, "last_pokeapi_request.txt")

  # Erase previous file
  if os.path.exists(filename):
    print(f"Removing previous 'last_pokeapi_request.txt' at '{filename}'...")
    os.remove(filename)

  print("Writing new file...\n")
  with open(filename, "a+") as file:
    file.write(str(request_time) + "\n")
    file.write(str(next_url) + "\n")
    file.write(str(previous_url) + "\n")
  
  return print("New file created.\n\n")
