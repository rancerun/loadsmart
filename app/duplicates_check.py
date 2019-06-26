# helpers to identify trucks carrying multiple loads and finding optimal solution instead 

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

def eliminate_duplicates(current_best_option, first_option, second_option, repeating_trucks):
  optimized_option = current_best_option
  duplicate_trucks_dict = {}

  for truck_name in repeating_trucks:
    duplicate_trucks_dict[truck_name] = []

  while duplicate_trucks_dict:
    for cargo, truck in first_option.items():
      current_truck = truck.keys()[0]
      duplicate_truck = duplicate_trucks_dict.keys()[-1]
      if current_truck == duplicate_truck:
        duplicate_trucks_dict[current_truck].append(cargo)

    duplicate_truck_info = duplicate_trucks_dict.popitem()
    
    duplicate_cargo = duplicate_truck_info[1]

    first_cargo = duplicate_cargo[0]
    second_cargo = duplicate_cargo[1]
    cargo1_first_option = first_option[first_cargo].values()[0]
    cargo2_first_option = first_option[second_cargo].values()[0]
    cargo1_second_option = second_option[first_cargo].values()[0]
    cargo2_second_option = second_option[second_cargo].values()[0]

    first_combination = cargo1_first_option + cargo2_second_option
    second_combination = cargo1_second_option + cargo2_first_option

    if min(first_combination, second_combination) == first_combination:
      optimized_option[first_cargo] = first_option[first_cargo]
      optimized_option[second_cargo] = second_option[second_cargo]
    else:
      optimized_option[first_cargo] = second_option[first_cargo]
      optimized_option[second_cargo] = first_option[second_cargo]
      
  return optimized_option