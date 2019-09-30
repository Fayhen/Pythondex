from server import db
import server.models as models
import server.queries as queries


def pre_populate_types():
  """
  This function populates the database with basic Pokémon
  types data. Execute this function only once, unless you
  have resetted the database.
  """
  normal = models.Types(name="normal")
  db.session.add(normal)

  fighting = models.Types(name="fighting")
  db.session.add(fighting)

  flying = models.Types(name="flying")
  db.session.add(flying)

  poison = models.Types(name="poison")
  db.session.add(poison)

  ground = models.Types(name="ground")
  db.session.add(ground)

  rock = models.Types(name="rock")
  db.session.add(rock)

  bug = models.Types(name="bug")
  db.session.add(bug)

  ghost = models.Types(name="ghost")
  db.session.add(ghost)
  
  steel = models.Types(name="steel")
  db.session.add(steel)

  fire = models.Types(name="fire")
  db.session.add(fire)

  water = models.Types(name="water")
  db.session.add(water)

  grass = models.Types(name="grass")
  db.session.add(grass)

  electric = models.Types(name="electric")
  db.session.add(electric)

  psychic = models.Types(name="psychic")
  db.session.add(psychic)

  ice = models.Types(name="ice")
  db.session.add(ice)

  dragon = models.Types(name="dragon")
  db.session.add(dragon)

  dark = models.Types(name="dark")
  db.session.add(dark)

  fairy = models.Types(name="fairy")
  db.session.add(fairy)

  db.session.commit()

  return print("Success.")


def pre_populate_gens():
  """
  This function populates the database with basic Pokémon
  generation data. Execute this function only once, unless
  you have resetted the database.
  """
  one = models.Generation(name="generation-i", region="kanto",
    games="Red and Green, Blue, Red and Blue, Yellow")
  db.session.add(one)

  two = models.Generation(name="generation-ii", region="johto",
    games="Gold and Silver, Crystal")
  db.session.add(two)

  three = models.Generation(name="generation-iii", region="hoenn",
    games="Ruby and Sapphire, FireRed and LeafGreen, Emerald")
  db.session.add(three)

  four = models.Generation(name="generation-iv", region="sinnoh",
    games="Diamond and Pearl, Platinum, HeartGold and SoulSilver")
  db.session.add(four)

  five = models.Generation(name="generation-v", region="unova",
    games="Black and White, Black 2 and White 2")
  db.session.add(five)

  six = models.Generation(name="generation-vi", region="kalos",
    games="X and Y, Omega Ruby and Alpha Sapphire")
  db.session.add(six)

  seven = models.Generation(name="generation-vii", region="alola",
    games="Sun and Moon, Ultra Sun and Ultra Moon, Let's Go, Pikachu! and Let's Go, Eevee!")
  db.session.add(seven)

  eight = models.Generation(name="generation-viii", region="galar",
    games="Sword and Shield")
  db.session.add(eight)

  db.session.commit()

  return print("Success.")


def pre_populate_habitats():
  """
  This function populates the database with basic Pokémon
  habitat data. Execute this function only once, unless you
  have resetted the database.
  """
  cave = models.Habitat(name="cave")
  db.session.add(cave)

  forest = models.Habitat(name="forest")
  db.session.add(forest)

  grassland = models.Habitat(name="grassland")
  db.session.add(grassland)

  mountain = models.Habitat(name="mountain")
  db.session.add(mountain)

  rare = models.Habitat(name="rare")
  db.session.add(rare)

  rough_terrain = models.Habitat(name="rough_terrain")
  db.session.add(rough_terrain)

  sea = models.Habitat(name="sea")
  db.session.add(sea)

  urban = models.Habitat(name="urban")
  db.session.add(urban)

  waters_edge = models.Habitat(name="waters_edge")
  db.session.add(waters_edge)

  db.session.commit()

  return print("Success.")


def pre_populate():
  """
  Pre-populates the database with Pokémon types, generations
  and habitats in succession. Either execute this function alone
  or the ones above individually, not both.
  """
  try:
    pre_populate_types()
    pre_populate_gens()
    pre_populate_habitats()
    return print("Success. Types, generations and habitats added to database.")
  except Exception as e:
    return e
