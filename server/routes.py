from flask import jsonify, request, make_response
from server import app, db
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
      return make_response(jsonify(schemas.pokemons_schema.dump(pokemons)), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/pokemons/<int:id>", methods=["GET"])
def get_pokemon(id):
  try:
    pokemon = queries.query_pokemon_id(id)
    if pokemon is None:
      err_msg = "This Pokémon couldn't be found. Have you captured it yet?"
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.pokemon_schema.dump(pokemon)), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/pokemons/<species>", methods=["GET"])
def get_pokemon_sp(species):
  try:
    pokemon = queries.query_pokemon_species(species)
    if pokemon is None:
      err_msg = "This Pokémon couldn't be found. Have you captured it yet?"
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.pokemon_schema.dump(pokemon)), 200)
  
  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/pokemons/<int:id>/evolution", methods=["GET"])
def get_pokemon_evolution(id):
  try:
    pokemon = queries.query_pokemon_id(id)
    if pokemon is None:
      err_msg = "Requested Pokémon couldn't be found. Have you captured it yet?"
      return make_response(err_msg, 404)
    else:
      evolution_chain = fetch.get_pokemon_evolution(pokemon)
      return make_response(jsonify(schemas.pokemons_schema.dump(evolution_chain)), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/generations", methods=["GET"])
def get_gens():
  try:
    gens = queries.query_gens()
    if gens is None:
      err_msg = "No generations found."
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.gens_schema.dump(gens)), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/generations/<int:id>", methods=["GET"])
def get_gen_id(id):
  try:
    gen = queries.query_pokemon_gen(id)
    if gen is None:
      err_msg = "Generation not found. Is it from the future? If not please contact the developer for this issue."
      make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.gen_schema.dump(gen)), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/generations/<region>", methods=["GET"])
def get_gen(region):
  try:
    gen = queries.query_pokemon_region(region)
    if gen is None:
      err_msg = "Region not found. Is it from the future? If not please contact the developer for this issue."
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.gen_schema.dump(gen)), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/generations/<int:id>/pokemons", methods=["GET"])
def get_gen_pokemons(id):
  try:
    pokemons = fetch.get_pokemons_of_gen(id)
    if pokemons is None:
      err_msg = "No Pokémons found. Have you catched any on this region?"
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(pokemons), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/types", methods=["GET"])
def get_types():
  try:
    types = queries.query_types()
    if types is None:
      err_msg = "No Pokémon types found."
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.types_schema.dump(types)), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/types/<int:id>", methods=["GET"])
def get_type(id):
  try:
    poke_type = queries.query_pokemon_type_id(id)
    if poke_type is None:
      err_msg = "Pokémon type not found. Please contact the developer for this issue."
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.type_schema.dump(poke_type)), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/types/<poke_type>", methods=["GET"])
def get_type_named(poke_type):
  try:
    poke_type = queries.query_pokemon_type(poke_type)
    if poke_type is None:
      err_msg = "Pokémon type not found. Was it typed right?"
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.type_schema.dump(poke_type)), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/types/<int:id>/pokemons", methods=["GET"])
def get_type_pokemons(id):
  try:
    pokemons = fetch.get_pokemons_of_type(id)
    if pokemons is None:
      err_msg = "No Pokémons of this type found. Have you catched any?"
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(pokemons), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/abilities", methods=["GET"])
def get_abilities():
  try:
    abilities = queries.query_abilities()
    if abilities is None:
      err_msg = "No Pokémon abilities found! Have you catched any yet? Else please contact the developer for this issue."
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.abilities_schema.dump(abilities)), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/abilities/<int:id>", methods=["GET"])
def get_ability(id):
  try:
    ability = queries.query_pokemon_ability_id(id)
    if ability is None:
      err_msg = "Ability not found. Have you caught a Pokémon with it yet? Else please contact the developer for this issue."
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.ability_schema.dump(ability)), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/abilities/<ability>", methods=["GET"])
def get_ability_named(ability):
  try:
    ability = queries.query_pokemon_ability(ability)
    if ability is None:
      err_msg = "Ability not found. Have you found a Pokémon that has it yet?"
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.ability_schema.dump(ability)), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/abilities/<int:id>/pokemons", methods=["GET"])
def get_ability_pokemons(id):
  try:
    pokemons = fetch.get_pokemons_with_ability(id)
    if pokemons is None:
      err_msg = "No Pokémons with this ability found. Have you found any that has it yet? Else, please contact the developer for this issue."
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(pokemons), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/habitats", methods=["GET"])
def get_habitats():
  try:
    habitats = queries.query_habitats()
    if habitats is None:
      err_msg = "No Pokémon habitats found."
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.habitats_schema.dump(habitats)), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/habitats/<int:id>", methods=["GET"])
def get_habitat_id(id):
  try:
    habitat = queries.query_pokemon_habitat_id(id)
    if habitat is None:
      err_msg = "Pokémon habitat not found. Please contact the developer for this issue."
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.habitat_schema.dump(habitat)), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/habitats/<habitat>", methods=["GET"])
def get_habitat_named(habitat):
  try:
    habitat = queries.query_pokemon_habitat(habitat)
    if habitat is None:
      err_msg = "Pokémon habitat not found. Was it typed right? Else, please contact the developer for this issue."
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.habitat_schema.dump(habitat)), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)


@app.route("/habitats/<int:id>/pokemons", methods=["GET"])
def get_habitat_pokemons(id):
  try:
    pokemons = fetch.get_pokemons_of_habitat(id)
    if pokemons is None:
      err_msg = "No Pokémons from this habitat found. Have you explored it?"
      return make_response(err_msg, 404)
    else:
      return make_response(jsonify(schemas.pokemons_schema.dump(pokemons)), 200)

  except Exception as e:
    return make_response("Internal error. Please contact the developer. Error:\n" + str(e), 500)



@app.route("/static/<path:path>")
def send_static():
  return send_from_directory('static', path)
