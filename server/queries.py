from server import db
from server.models import (Types, Abilities, 
  Generation, Pokemon)


def gotta_catch_em_all():
  """
  Returns all Pokémons from the database.
  """
  return Pokemon.query.all()


def query_pokemon_id(id):
  """
  Returns Pokémon by its id on the database.
  """
  return Pokemon.query.get(id)


def query_pokemon_species(species):
  """
  Returns Pokémon by its species name. Argument 'species'
  should be string containing the species name. Ex.:
  'mewtwo'.
  """
  return Pokemon.query.filter_by(species=species).all()


def query_pokemon_type(poke_type):
  """
  Returns type by its name, including its current available
  Pokémons. Argument 'types' should be string containing a
  single Pokémon type. Ex.: 'normal'.
  """
  return Types.query.filter_by(name=poke_type).all()


def query_pokemon_gen(generation):
  """
  Returns generation by generation the name, including its
  current available Pokémons. Argument 'generation' should
  be string containing generation representation in roman
  numerals. Ex.: 'iii'.
  """
  return Generation.query.filter_by(name=generation).all()


def query_pokemon_region(region):
  """
  Returns generation by generation its region's name, including
  its current available Pokémons. Argument 'region' should be
  string containing a single region name. Ex.: 'hoenn'.
  """
  return Generation.query.filter_by(region=region).all()


def query_pokemon_ability(ability):
  """
  Returns a Pokémon  ability by its name, including all Pokémons
  currently possessing it. Argument 'ability' should be string
  contaning a single ability name. Ex.: 'splash'.
  """
  return Abilities.query.filter_by(name=ability).all()


def query_types():
  """
  Returns all Pokémon types on the database.
  """
  return Types.query.all()


def query_gens():
  """
  Returns all Pokémon generations on the database.
  """
  return Generation.query.all()


def query_abilities():
  """
  Returns all Pokémon abilities on the database.
  """
  return Abilities.query.all()
