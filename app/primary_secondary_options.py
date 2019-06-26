# determine shortest & second shortest overall distance for each cargo

import calculations as cal

def primary_secondary_options(cargos, trucks):
  first_option = {} 
  second_option = {}

  for cargo_name, cargo_info in cargos.items():
    first_option[cargo_name] = {'null': float('inf')}
    second_option[cargo_name] = {'null': float('inf')}

    for truck_name, truck_info in trucks.items():
      first_option_truck_distance = first_option[cargo_name].values()[0]
      second_option_truck_distance = second_option[cargo_name].values()[0]

      truck_to_origin_distance = cal.calculate_distance(truck_info['lng'], truck_info['lat'], cargo_info['o_lng'], cargo_info['o_lat'])
      truck_to_end_distance = cal.calculate_distance(truck_info['lng'], truck_info['lat'], cargo_info['d_lng'], cargo_info['d_lat'])
      current_truck_distance = truck_to_origin_distance + truck_to_end_distance

      if first_option_truck_distance > current_truck_distance:
        second_option[cargo_name] = first_option[cargo_name]
        first_option[cargo_name] = {
          truck_name: current_truck_distance
        }
      elif second_option_truck_distance > current_truck_distance:
        second_option[cargo_name] = {
          truck_name: current_truck_distance
        }
  return first_option, second_option