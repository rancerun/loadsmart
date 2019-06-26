import unittest
import sys
sys.path.append('../app')
from primary_secondary_options import primary_secondary_options

class TestPrimarySecondaryOptions(unittest.TestCase):

  def setUp(self):
    print('setup')
    self.cargos = {
      'A': {'o_lat': 44.4582983, 'o_lng': -93.161604, 'd_lat': 42.3636331, 'd_lng': -87.8447938},
      'B': {'o_lat': 38.8951, 'o_lng': -77.0363, 'd_lat': 39.9624, 'd_lng': -76.7274},
      'C': {'o_lat': 39.9524, 'o_lng': -75.1636, 'd_lat': 43.1031, 'd_lng': -79.0303},
      'D': {'o_lat': 1, 'o_lng': 1, 'd_lat': 45, 'd_lng': 13}
    }
    self.trucks = {
      'Banana Boat': {'lat': 5, 'lng': 4},
      'Windfall': {'lat': -79.406307, 'lng': 0.314931},
      'Coffee Beans': {'lat': -6.86997, 'lng': -75.045851},
      'Batmobile': {'lat': 40.741895, 'lng': -73.989308},
      'Chariot': {'lat': 41.894802, 'lng': 30.485338},
      'Caramel Swirls': {'lat': 47.372394, 'lng': 8.542333},
      'Zebra Stripes': {'lat': -1.283253, 'lng': 36.817245},
      'Slam Dunk': {'lat': 35.682839, 'lng': 139.759455},
      'Alfredo': {'lat': 42.6011194, 'lng': -89.6384532}
    }

  def tearDown(self):
    print('teardown')

  def test_primary_secondary_options(self):
    self.assertEqual(primary_secondary_options(self.cargos, self.trucks), (
      {
        'A': {'Alfredo': 5.79198868163568},
        'C': {'Batmobile': 6.981600672073832},
        'B': {'Batmobile': 6.409864033717816},
        'D': {'Banana Boat': 46.0}
      },
      {
        'A': {'Batmobile': 33.47924517190808},
        'C': {'Alfredo': 25.335222757961162},
        'B': {'Alfredo': 26.31372612524318},
        'D': {'Caramel Swirls': 52.031417601311496}
      }))

if __name__ == '__main__':
  unittest.main()