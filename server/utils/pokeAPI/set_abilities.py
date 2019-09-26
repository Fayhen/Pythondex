from server import db
import requests
import server.models as models


def run(all_ability_urls):
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

  # Iterate and request data from Pokémon ability URLs
  for url in all_ability_urls:
    print(f"Fetching: '{url}'.")
    r = requests.get(url)
    response_data = r.json()

    # Retrieve ability name from response data
    name = response_data["name"]
    print(f"Retrieved ability: '{name}'.")

    # Check database for existing ability
    queried_ability = models.Abilities.query.filter_by(name=name).first()

    # Add ability to database when unexistant
    if queried_ability is None:
      new_ability = models.Abilities(name=name,
        description=response_data["effect_entries"][0]["effect"])
      
      db.session.add(new_ability)
      db.session.commit()

      # Add new ability 'id' to abilities list
      abilities.append(new_ability.id)

      print("Added to db.\n")
    
    else:
      # Add existing ability 'id' to abilities list
      abilities.append(queried_ability.id)
      print("Already on db.\n")
  
  # Return ability 'id' list
  return abilities
  