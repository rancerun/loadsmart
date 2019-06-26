#checks for edge cases with the same truck as the best option for multiple cargos

import sys
sys.path.append('.')
from eliminate_duplicates import eliminate_duplicates

def repeating_truck_check(first_option, second_option):
  used_trucks = set()
  repeating_trucks = set()

  for cargo_name in first_option:
    current_best_truck = first_option[cargo_name].keys()[0]

    if current_best_truck not in used_trucks:
      used_trucks.add(current_best_truck)
    else:
      repeating_trucks.add(current_best_truck)

  return repeating_trucks