from server import ma
import server.models as models


class PokemonRestricted(ma.ModelSchema):
  class Meta:
    model = models.Pokemon
    fields = ("id", "species", "url")
  
  url = ma.URLFor("get_pokemon", id="<id>", _scheme="http", _external=True)

class TypesSchema(ma.ModelSchema):
  class Meta:
    model = models.Types

  url = ma.URLFor("get_type", id="<id>", _scheme="http", _external=True)
  pokemon = ma.Nested(PokemonRestricted, many=True)

class AbilitiesSchema(ma.ModelSchema):
  class Meta:
    model = models.Abilities

  url = ma.URLFor("get_ability", id="<id>", _scheme="http", _external=True)
  pokemon = ma.Nested(PokemonRestricted, many=True)

class GenerationSchema(ma.ModelSchema):
  class Meta:
    model = models.Generation

  url = ma.URLFor("get_gen", id="<id>", _scheme="http", _external=True)
  pokemon = ma.Nested(PokemonRestricted, many=True)

class HabitatShema(ma.ModelSchema):
  class Meta:
    model = models.Habitat

  url = ma.URLFor("get_habitat", id="<id>", _scheme="http", _external=True)
  pokemon = ma.Nested(PokemonRestricted, many=True)

class PokemonSchema(ma.ModelSchema):
  class Meta:
    model = models.Pokemon

  url = ma.URLFor("get_pokemon", id="<id>", _scheme="http", _external=True)
  types = ma.Nested(TypesSchema, only=("id", "name", "url"), many=True)
  abilities = ma.Nested(AbilitiesSchema, only=("id", "name", "url"), many=True)
  generation = ma.Nested(GenerationSchema, only=("id", "name", "url"), many=True)
  habitat = ma.Nested(HabitatShema, only=("id", "name", "url"), many=True)


# Schemas initialization
type_schema = TypesSchema()
types_schema = TypesSchema(many=True)
ability_schema = AbilitiesSchema()
abilities_schema = AbilitiesSchema(many=True)
gen_schema = GenerationSchema()
gens_schema = GenerationSchema(many=True)
habitat_schema = HabitatShema()
habitats_schema = HabitatShema(many=True)
pokemon_schema = PokemonSchema()
pokemons_schema = PokemonSchema(many=True)
