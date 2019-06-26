#using Python 2.7.10

import sys
sys.path.append('../static')
from data import cargos, trucks

import sys
sys.path.append('.')
from primary_secondary_options import primary_secondary_options
from repeating_truck_check import repeating_truck_check
from eliminate_duplicates import eliminate_duplicates

def shortest_distance(cargos, trucks):
  best_option = {}
  
  first_option, second_option = primary_secondary_options(cargos, trucks)

  repeating_trucks = repeating_truck_check(first_option, second_option)

  for cargo_name, truck_info in first_option.items():
    current_best_truck = first_option[cargo_name].keys()[0]

    if current_best_truck not in repeating_trucks:
      best_option[cargo_name] = truck_info

  if repeating_trucks:
    best_option_minus_repeating_trucks = eliminate_duplicates(best_option, first_option, second_option, repeating_trucks)
    return best_option_minus_repeating_trucks
  else:
    return best_option


print(shortest_distance(cargos, trucks))