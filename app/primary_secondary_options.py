# determine shortest & second shortest overall distance for each cargo

import calculations as cal

def primary_secondary_options(cargos, trucks):
  cargo_options = {}

  for cargo_name, cargo_info in cargos.items():
    cargo_options[cargo_name] = [{'null': float('inf')}, {'null': float('inf')}]

    for truck_name, truck_info in trucks.items():
      first_option_distance = cargo_options[cargo_name][0].values()[0]
      second_option_distance = cargo_options[cargo_name][1].values()[0]

      truck_to_origin_distance = cal.calculate_distance(truck_info['lng'], truck_info['lat'], cargo_info['o_lng'], cargo_info['o_lat'])
      truck_to_end_distance = cal.calculate_distance(truck_info['lng'], truck_info['lat'], cargo_info['d_lng'], cargo_info['d_lat'])
      current_truck_distance = truck_to_origin_distance + truck_to_end_distance

      if first_option_distance > current_truck_distance:
        cargo_options[cargo_name][1] = cargo_options[cargo_name][0]
        cargo_options[cargo_name][0] = {
          truck_name: current_truck_distance
        }
      elif second_option_distance > current_truck_distance:
        cargo_options[cargo_name][1] = {
          truck_name: current_truck_distance
        }

  return cargo_options