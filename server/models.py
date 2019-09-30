from server import db


class Types(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, unique=True, nullable=False)
  pokemon = db.relationship("Pokemon",
    secondary=lambda: helper_pokemon_type, back_populates="types")


class Abilities(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, unique=True, nullable=False)
  description = db.Column(db.String(120), nullable=False)
  pokemon = db.relationship("Pokemon",
    secondary=lambda: helper_pokemon_ability, back_populates="abilities")


class Generation(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, unique=True, nullable=False)
  region = db.Column(db.String, unique=True, nullable=False)
  games = db.Column(db.String(120), nullable=False)
  pokemon = db.relationship("Pokemon",
    secondary=lambda: helper_pokemon_generation, back_populates="generation")


class Habitat(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, unique=True, nullable=False)
  pokemon = db.relationship("Pokemon",
      secondary=lambda: helper_pokemon_habitat, back_populates="habitat")

class Pokemon(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  species = db.Column(db.String, unique=True, nullable=False)
  description = db.Column(db.String(120), nullable=False)
  height = db.Column(db.Integer, nullable=False)
  weight = db.Column(db.Integer, nullable=False)
  base_experience = db.Column(db.Integer, nullable=False)
  base_hp = db.Column(db.Integer, nullable=False)
  base_attack = db.Column(db.Integer, nullable=False)
  base_defense = db.Column(db.Integer, nullable=False)
  base_speed = db.Column(db.Integer, nullable=False)
  base_sp_atk = db.Column(db.Integer, nullable=False)
  base_sp_def = db.Column(db.Integer, nullable=False)
  evolves_from = db.Column(db.String, nullable=True)
  evolves_into = db.Column(db.String, nullable=True)
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
  habitat = db.relationship("Habitat",
    secondary = lambda: helper_pokemon_habitat,
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


helper_pokemon_habitat = db.Table("helper_pokemon_habitat",
  db.Column("pokemon", db.Integer, db.ForeignKey(Pokemon.id)),
  db.Column("habitat", db.Integer, db.ForeignKey(Habitat.id))
)
