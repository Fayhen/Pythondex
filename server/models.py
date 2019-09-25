from server import db


class Types(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, unique=True)
  pokemon = db.relationship("Pokemon",
    secondary=lambda: helper_pokemon_type, back_populates="types")


class Abilities(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, unique=True)
  description = db.Column(db.String(120))
  pokemon = db.relationship("Pokemon",
    secondary=lambda: helper_pokemon_ability, back_populates="abilities")


class Generation(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, unique=True)
  region = db.Column(db.String, unique=True)
  games = db.Column(db.String(120))
  pokemon = db.relationship("Pokemon",
    secondary=lambda: helper_pokemon_generation, back_populates="generation")


class Pokemon(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  species = db.Column(db.String, unique=True)
  description = db.Column(db.String(120))
  height = db.Column(db.Integer)
  weight = db.Column(db.Integer)
  base_attack = db.Column(db.Integer)
  base_defense = db.Column(db.Integer)
  base_speed = db.Column(db.Integer)
  base_sp_atk = db.Column(db.Integer)
  base_sp_def = db.Column(db.Integer)
  types = db.relationship("Types",
    secondary = lambda: helper_pokemon_type,
    back_populates = "pokemon"
  )
  abilities = db.relationship("Abilities",
    secondary = lambda: helper_pokemon_ability,
    back_populates = "pokemon"
  )
  generation = db.relationship("Generation",
    secondary = lambda: helper_pokemon_generation,
    back_populates= "pokemon"
  )


helper_pokemon_type = db.Table("helper_pokemon_type",
  db.Column("pokemon", db.Integer, db.ForeignKey(Pokemon.id)),
  db.Column("type", db.Integer, db.ForeignKey(Types.id))
)


helper_pokemon_ability = db.Table("helper_pokemon_ability",
  db.Column("pokemon", db.Integer, db.ForeignKey(Pokemon.id)),
  db.Column("ability", db.Integer, db.ForeignKey(Abilities.id))
)


helper_pokemon_generation = db.Table("helper_pokemon_generation",
  db.Column("pokemon", db.Integer, db.ForeignKey(Pokemon.id)),
  db.Column("generation", db.Integer, db.ForeignKey(Generation.id))
)
