# helpers to identify trucks carrying multiple loads and finding optimal solution instead 

def repeating_truck_check(cargo_options):
  used_trucks = set()
  repeating_trucks = set()

  for cargo_name in cargo_options:
    current_best_truck = cargo_options[cargo_name][0].keys()[0]

    if current_best_truck not in used_trucks:
      used_trucks.add(current_best_truck)
    else:
      repeating_trucks.add(current_best_truck)

  return repeating_trucks

def eliminate_duplicates(current_best_option, cargo_options, repeating_trucks):
  optimized_option = current_best_option
  duplicate_trucks_dict = {}

  for truck_name in repeating_trucks:
    duplicate_trucks_dict[truck_name] = []

  while duplicate_trucks_dict:
    duplicate_truck = duplicate_trucks_dict.keys()[-1]
    for cargo_name, trucks in cargo_options.items():
      current_truck = trucks[0].keys()[0]
      if current_truck == duplicate_truck:
        duplicate_trucks_dict[current_truck].append(cargo_name)

    duplicate_truck_info = duplicate_trucks_dict.popitem()
    
    duplicate_cargo = duplicate_truck_info[1]

    first_cargo = duplicate_cargo[0]
    second_cargo = duplicate_cargo[1]

    cargo1_first_option = cargo_options[first_cargo][0]
    cargo1_second_option = cargo_options[first_cargo][1]
    cargo2_first_option = cargo_options[second_cargo][0]
    cargo2_second_option = cargo_options[second_cargo][1]

    first_combination = cargo1_first_option.values()[0] + cargo2_second_option.values()[0]
    second_combination = cargo1_second_option.values()[0] + cargo2_first_option.values()[0]

    if min(first_combination, second_combination) == first_combination:
      optimized_option[first_cargo] = cargo1_first_option
      optimized_option[second_cargo] = cargo2_second_option
    else:
      optimized_option[first_cargo] = cargo1_second_option
      optimized_option[second_cargo] = cargo2_first_option
      
  return optimized_option