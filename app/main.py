from static.data import cargos, trucks
from primary_secondary_options import primary_secondary_options
import duplicates_check as dc

def shortest_distance(cargos, trucks):
  best_option = {}
  
  first_option, second_option = primary_secondary_options(cargos, trucks)

  repeating_trucks = dc.repeating_truck_check(first_option, second_option)

  for cargo_name, truck_info in first_option.items():
    current_best_truck = first_option[cargo_name].keys()[0]

    if current_best_truck not in repeating_trucks:
      best_option[cargo_name] = truck_info

  if repeating_trucks:
    best_option_minus_repeating_trucks = dc.eliminate_duplicates(best_option, first_option, second_option, repeating_trucks)
    return best_option_minus_repeating_trucks
  else:
    return best_option


print(shortest_distance(cargos, trucks))