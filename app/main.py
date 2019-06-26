from static.data import cargos, trucks
from primary_secondary_options import primary_secondary_options
import duplicates_check as dc

def shortest_distance(cargos, trucks):
  best_option = {}
  
  cargo_options = primary_secondary_options(cargos, trucks)

  repeating_trucks = dc.repeating_truck_check(cargo_options)

  for cargo_name, trucks in cargo_options.items():
    current_best_truck = trucks[0].keys()[0]

    if current_best_truck not in repeating_trucks:
      best_option[cargo_name] = trucks[0]

  if repeating_trucks:
    best_option_minus_repeating_trucks = dc.eliminate_duplicates(best_option, cargo_options, repeating_trucks)
    return best_option_minus_repeating_trucks
  else:
    return best_option

  return best_option

print(shortest_distance(cargos, trucks))