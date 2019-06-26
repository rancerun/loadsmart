import unittest
import sys
sys.path.append('../app')
from repeating_truck_check import repeating_truck_check

class TestDetermineBestOption(unittest.TestCase):

  def setUp(self):
    print('setup')
    self.first_option = {
      'A': {'Alfredo': 5.79198868163568},
      'C': {'Batmobile': 6.981600672073832},
      'B': {'Batmobile': 6.409864033717816},
      'D': {'Banana Boat': 46.0}
    }
    self.second_option = {
      'A': {'Batmobile': 33.47924517190808},
      'C': {'Alfredo': 25.335222757961162},
      'B': {'Alfredo': 26.31372612524318},
      'D': {'Caramel Swirls': 52.031417601311496}
    }

  def tearDown(self):
    print('teardown')

  def test_repeating_truck_check(self):
    self.assertEqual(repeating_truck_check(self.first_option, self.second_option),
      (set(['Batmobile'])))

if __name__ == '__main__':
  unittest.main()