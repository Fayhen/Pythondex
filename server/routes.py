from flask import jsonify, request, make_response
from server import db
import server.queries as queries
import server.schemas as schemas
import server.utils.GET_utils as fetch


@app.route("/pokemons/all", methods=["GET"])
def gotta_catch_em_all():
  try:
    pokemons = queries.gotta_catch_em_all()
    if pokemons is None:
      err_msg = "No Pokémons found! have you spoke with the Professor yet?"
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.pokemons_schema.dump(pokemons), 200))

  except:
    return make_response("Internal error. Please contact the developer.", 500)


@app.route("/pokemons/<int:id>", methods=["GET"])
def get_pokemon(id):
  try:
    pokemon = queries.query_pokemon_id(id)
    if pokemon is None:
      err_msg = "This Pokémon couldn't be found. Have you captured it yet?"
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.pokemon_schema(pokemon)), 200)

  except:
    return make_response("Internal error. Please contact the developer.", 500)


@app.route("/pokemons/<str:species>", methods=["GET"])
def get_pokemon_sp(species):
  try:
    pokemon = queries.query_pokemon_species(species)
    if pokemon is None:
      err_msg = "This Pokémon couldn't be found. Have you captured it yet?"
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.pokemon_schema.dump(pokemon)), 200)
  
  except:
    return make_response("Internal error. Please contact the developer.", 500)


@app.route("/generations", methods=["GET"])
def get_gens():
  try:
    generations = queries.query_gens()
    if generations is None:
      err_msg = "No generations found. Please contact the developer for this issue."
      return make_response(err_msg, 500)
    else:
      return make_response(jsonify(schemas.gens_schema), 200)

  except:
    return make_response("Internal error. Please contact the developer.", 500)


@app.route("/generations/<int:id>", methods=["GET"])
def get_gen(id):
  try:
    gen = queries.query_pokemon_gen(id):
    if gen is None:
      err_msg = "Region not found. Is it from the future? If not please contact the developer for this issue."
      make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.gen_schema.dump(gen)), 200)

  except:
    return make_response("Internal error. Please contact the developer.", 500)


@app.route("/generations/<str:region>", methods=["GET"])
def get_gen(region):
  try:
    gen = queries.query_pokemon_region(region)
    if gen is None:
      err_msg = "Region not found. Is it from the future? If not please contact the developer for this issue."
      make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.gen_schema.dump(gen)), 200)

  except:
    return make_response("Internal error. Please contact the developer.", 500)


@app.route("/generations/<int:id>/pokemons", methods=["GET"])
def get_gen_pokemons(id):
  try:
    pokemons = fetch.get_pokemons_of_gen(id)
    if len(pokemons) > 1:
      return make_response(jsonify(pokemons), 200)
    else:
      err_msg = "No Pokémons found. Have you catched any on this region?"
      return make_response(err_msg, 404)

  except:
    return make_response("Internal error. Please contact the developer.", 500)


@app.route("/types", methods=["GET"])
def get_types():
  try:
    types = queries.query_types()
    if types is None:
      err_msg = "No Pokémon types found. Please contact the developer for this issue."
      return make_response(err_msg, 500)
    else:
      return make_response(jsonify(schemas.types_schema.dump(types)), 200)

  except:
    return make_response("Internal error. Please contact the developer.", 500)


@app.route("/types/<int:id>", methods=["GET"])
def get_type(id):
  try:
    poke_type = queries.query_pokemon_type_id(id)
    if poke_type is None:
      err_msg = "Pokémon type not found. Please contact the developer for this issue."
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.type_schema.dump(poke_type)), 200)

  except:
    return make_response("Internal error. Please contact the developer.", 500)


@app.route("/types/<str:poke_type>", methods=["GET"])
def get_type_named(poke_type):
  try:
    poke_type = queries.query_pokemon_type(poke_type)
    if poke_type is None:
      err_msg = "Pokémon type not found. Was it typed right?"
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.type_schema.dump(poke_type)), 200)

  except:
    return make_response("Internal error. Please contact the developer.", 500)


@app.route("/types/<int:id>/pokemons", methods=["GET"])
def get_type_pokemons(id):
  try:
    pokemons = fetch.get_pokemons_of_type(id)
    if len(pokemons) > 1:
      return make_response(jsonify(pokemons), 200)
    else:
      err_msg = "No Pokémons of this type found. Have you catched any?"
      return make_response(err_msg, 404)

  except:
    return make_response("Internal error. Please contact the developer.", 500)


@app.route("/abilities", methods=["GET"])
def get_abilities():
  try:
    abilities = queries.query_abilities()
    if abilities is None:
      err_msg = "No Pokémon abilities found! have you catched one yet? Else please contact the developer for this issue."
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.abilities_schema.dump(abilities))), 200)

  except:
    return make_response("Internal error. Please contact the developer.", 500)


@app.route(("/abilities/<int:id>", methods=["GET"]))
def get_ability(id):
  try:
    ability = queries.query_pokemon_ability_id(id)
    if ability is None:
      err_msg = "Ability 'id' not found. Please contact the developer for this issue."
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.ability_schema.dump(ability)), 200)

  except:
    return make_response("Internal error. Please contact the developer.", 500)


@app.route(("/abilities/<str:ability>", methods=["GET"]))
def get_ability_named(ability):
  try:
    ability = queries.query_pokemon_ability(ability)
    if ability is None:
      err_msg = "Ability not found. Have you found a Pokémon that has it yet?"
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.ability_schema.dump(ability)), 200)

  except:
    return make_response("Internal error. Please contact the developer.", 500)


@app.route(("/abilities/<int:id>/pokemons", methods=["GET"]))
def get_ability_pokemons(id):
  try:
    pokemons = fetch.get_pokemons_with_ability(id)
    if len(pokemons) > 1:
      return make_response(jsonify(pokemons), 200)
    else:
      err_msg = "No Pokémons with this ability found. Have you found any that has it yet? Else, please contact the developer for this issue."
      return make_response(err_msg, 404)

  except:
    return make_response("Internal error. Please contact the developer.", 500)
