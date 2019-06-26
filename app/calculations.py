from math import sqrt

def pythagorean(edge1, edge2):
  return sqrt((edge1 ** 2) + (edge2 ** 2))

def calculate_distance(lng1, lat1, lng2, lat2):
  lng_dif = lng2 - lng1
  lat_dif = lat2 - lat1
  return pythagorean(lng_dif, lat_dif)