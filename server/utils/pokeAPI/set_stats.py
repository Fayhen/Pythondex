def run(all_stats):
  """
  This helper function receives and iterates over an object of base stats retrieved
  from PokéAPI, for the current Pokémon instance. At each iteration the stat
  name is checked for and set accordingly. A dict with the base stats is returned.
  """
  print("Entered 'all_stats' function.")
  base_stats = {}

  # Retrieve stat values from stats object
  print("Entering 'all_stats' loop.\n")
  for stat_data in all_stats:
    if stat_data["stat"]["name"] == "speed":
      base_stats["base_speed"] = stat_data["base_stat"]
      print("Got speed.")

    elif stat_data["stat"]["name"] == "special-defense":
      base_stats["base_sp_def"] = stat_data["base_stat"]
      print("Got special-defense.")

    elif stat_data["stat"]["name"] == "special-attack":
      base_stats["base_sp_atk"] = stat_data["base_stat"]
      print("Got special-attack.")

    elif stat_data["stat"]["name"] == "defense":
      base_stats["base_defense"] = stat_data["base_stat"]
      print("Got defense.")

    elif stat_data["stat"]["name"] == "attack":
      base_stats["base_attack"] = stat_data["base_stat"]
      print("Got attack.")

    else:
      base_stats["base_hp"] = stat_data["base_stat"]
      print("Got health points.")
  
  print(f"Returning:\n{base_stats}.")
  return base_stats
