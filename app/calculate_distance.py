import sys
sys.path.append('./')
from pythagorean import pythagorean

def calculate_distance(lng1, lat1, lng2, lat2):
  lng_dif = lng2 - lng1
  lat_dif = lat2 - lat1
  return pythagorean(lng_dif, lat_dif)