from server import db

class Types(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  pokemon = db.relationship("Pokemon", backref="pokemon_type", lazy=True)

class Abilities(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  description = db.Coumn(db.String)
  pokemon = db.relationship("Pokemon", backref="pokemon_ability", lazy=True)

class Generation(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  region = db.Coumn(db.String)
  games = db.Column(db.String)
  pokemon = db.relationship("Pokemon", backref="pokemon_game", lazy=True)

class Pokemon(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  species = db.Column(db.String)
  description = db.Column(db.String)
  height = db.Column(db.Integer)
  weight = db.Column(db.Integer)
  base_attack = db.Column(db.Integer)
  base_defense = db.Column(db.Integer)
  base_speed = db.Column(db.Integer)
  base_sp_atk = db.Column(db.Integer)
  base_sp_def = db.Column(db.Integer)
  types = db.relationship("Types",
    secondary = lambda: helper_pokemon_type,
    back_populates = "pokemons"
  )
  abilities = db.relationship("Abilities",
    secondary = lambda: helper_pokemon_ability,
    back_populates = "pokemons"
  )
  generation = db.relationship("Generation",
    secondary = lambda: helper_pokemon_generation,
    back_populates: 'pokemons'
  )

helper_pokemon_type = db.Table("helper_pokemon_type",
  db.Column("pokemon", db.Integer, db.ForeignKey(Pokemon.id)),
  db.Column("type", db.Integer, db.ForeignKey(Types.id))
)

helper_pokemon_ability = db.Table("helper_pokemon_ability",
  db.Column("pokemon", db.Integer, db.ForeignKey(Pokemon.id)),
  db.Column("ability", db.Integer, db.ForeignKey(Types.id))
)

helper_pokemon_generation = db.Table("helper_pokemon_generation",
  db.Column("pokemon", db.Integer, db.ForeignKey(Pokemon.id)),
  db.Column("generation", db.Integer, db.ForeignKey(Generation.id))
)
