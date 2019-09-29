from server import ma
import server.models as models


class TypesSchema(ma.ModelSchema):
  class Meta:
    model = models.Types

class AbilitiesSchema(ma.ModelSchema):
  class Meta:
    model = models.Abilities

class GenerationSchema(ma.ModelSchema):
  class Meta:
    model = models.Generation

class PokemonSchema(ma.ModelSchema):
  class Meta:
    model = models.Pokemon


# Schemas initialization
type_schema = TypesSchema()
types_schema = TypesSchema(many=True)
ability_schema = AbilitiesSchema()
abilities_schema = AbilitiesSchema(many=True)
gen_schema = GenerationSchema()
gens_schema = GenerationSchema(many=True)
pokemon_schema = PokemonSchema()
pokemons_schema = PokemonSchema(many=True)
