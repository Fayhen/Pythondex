import os
from datetime import datetime, timedelta
from server import app


def run(continue_from_last):
  """
  Sets up initial request based on the argument passed on the main outer
  function.
  """
  # Ensure path exists
  filepath = os.path.join(app.root_path, "utils", "temp")
  if not os.path.exists(filepath):
    os.makedirs(filepath)

  # Get next URL from file if 'True'
  if continue_from_last:
    filename = os.path.join(filepath, "last_pokeapi_request.txt")
    print(f"\n\nRetrieving URL from file at '{filename}'...")

    with open(filename, "r") as file:
      lines = file.read().splitlines()
      date_string = lines[0]
      base_url = lines[1]
      print(f"Last PokéAPI request was issued at: '{date_string}'.")
      print(f"Next URL: '{base_url}'.")

    # Parse last request time into Python's datetime object
    python_time = datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S %Z")
    
    # Ensure minimun time elapsed between requests
    elapsed = datetime.utcnow() - python_time
    if elapsed.seconds > 60:
      return base_url
    else:
      raise Exception("Not enough time has passed between requests to PokéAPI.")

  # Return default base URL if 'False'
  else:
    return "https://pokeapi.co/api/v2/pokemon/?limit=19/"  
