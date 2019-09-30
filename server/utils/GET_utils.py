import server.queries as queries
import server.schemas as schemas
from server.models import Pokemon

"""
Functions within this file are provided in order to reduce
code inside routing functions, in cases where query objects
require a little more data manipulation before sending
responses to GET requests.
"""


def get_pokemons_of_gen(id):
  """
  Queries a Pokémon generation using the 'id' passed as argument.
  Iterates over the foreign keys listed on the 'pokemon' table
  column. At each iteration, queries the Pokémon and stores its
  data in a variable. This data is then serialized and appended
  to an array, which is returned by the function. This array can
  be readily passed to Flask's 'jsonify' function when sending
  HTTP responses.
  """
  gen = queries.query_pokemon_gen(id)
  if gen is None:
    return None
  else:
    pokemons = gen.pokemon
    pokemon_data = []
    # 'pokemons' is already a list of queried Pokémons, thanks to SQLAlchemy:
    for pokemon in pokemons:
      pokemon_data.append(schemas.pokemon_schema.dump(pokemon))

    return pokemon_data


def get_pokemons_of_type(id):
  """
  Queries a Pokémon type using the 'id' passed as argument.
  Iterates over the foreign keys listed on the 'pokemon' table
  column. At each iteration, queries the Pokémon and stores its
  data in a variable. This data is then serialized and appended
  to an array, which is returned by the function. This array can
  be readily passed to Flask's 'jsonify' function when sending
  HTTP responses.
  """
  poke_type = queries.query_pokemon_type_id(id)
  if poke_type is None:
    return None
  else:
    pokemons = poke_type.pokemon
    pokemon_data = []
    # 'pokemons' is already a list of queried Pokémons, thanks to SQLAlchemy:
    for pokemon in pokemons:
      pokemon_data.append(schemas.pokemon_schema.dump(pokemon))

    return pokemon_data


def get_pokemons_of_habitat(id):
  """
  Queries Pokémon from a habitat using the 'id' passed as argument.
  Iterates over the foreign keys listed on the 'pokemon' table
  column. At each iteration, queries the Pokémon and stores its
  data in a variable. This data is then serialized and appended
  to an array, which is returned by the function. This array can
  be readily passed to Flask's 'jsonify' function when sending
  HTTP responses.
  """
  habitat = queries.query_pokemon_habitat_id(id)
  if habitat is None:
    return None
  else:
    pokemons = habitat.pokemon
    pokemon_data = []
    # 'pokemons' is already a list of queried Pokémons, thanks to SQLAlchemy:
    for pokemon in pokemons:
      pokemon_data.append(schemas.pokemon_schema.dump(pokemon))

    return pokemon_data


def get_pokemons_with_ability(id):
  """
  Queries a Pokémon ability using the 'id' passed as argument.
  Iterates over the foreign keys listed on the 'pokemon' table
  column. At each iteration, queries the Pokémon and stores its
  data in a variable. This data is then serialized and appended
  to an array, which is returned by the function. This array can
  be readily passed to Flask's 'jsonify' function when sending
  HTTP responses.
  """
  ability = queries.query_pokemon_ability_id(id)
  if ability is None:
    return None
  else:
    pokemons = ability.pokemon
    pokemon_data = []
    # 'pokemons' is already a list of queried Pokémons, thanks to SQLAlchemy:
    for pokemon in pokemons:
      # raw_data = queries.query_pokemon_id(pokemon)
      pokemon_data.append(schemas.pokemon_schema.dump(pokemon))

    return pokemon_data


def get_pokemon_evolution(pokemon):
  """
  Returns a Pokémon's evolution chain represented as a list
  of the Pokémons evolutionary stages, previous and past.
  Returns a list with single Pokémon if it has no other forms.
  Receives a queried Pokemon object as argument.
  """
  def query_stage(species):
    """
    Called to return either a previous or next evolution of the
    current Pokémon, based on its respective species name.
    """
    stage = Pokemon.query.filter_by(species=species).first()

    return stage
  
  evolution_chain = []
  evolution_chain.append(pokemon)

  while True:
    if pokemon.evolves_from:
      pokemon = query_stage(pokemon.evolves_from)
      evolution_chain.append(pokemon)
    else:
      break

  while True:
    if pokemon.evolves_into:
      pokemon = query_stage(pokemon.evolves_into)
      evolution_chain.append(pokemon)
    else:
      break
  
  return evolution_chain
