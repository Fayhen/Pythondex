import server.models as models


def run(all_types):
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
