import sys
import os
import unittest
sys.path.append(os.path.abspath('../app'))
import app.duplicates_check as dc

class TestDuplicatesCheck(unittest.TestCase):
  def setUp(self):
    print('setup')
    self.cargo_options = {
      'A': [{'Alfredo': 5.79198868163568}, {'Batmobile': 33.47924517190808}],
      'C': [{'Batmobile': 6.981600672073832}, {'Alfredo': 25.335222757961162}],
      'B': [{'Batmobile': 6.409864033717816}, {'Alfredo': 26.31372612524318}],
      'D': [{'Banana Boat': 46.0}, {'Caramel Swirls': 52.031417601311496}]}
    self.best_options = {
      'A': {'Alfredo': 5.79198868163568},
      'D': {'Banana Boat': 46.0}}
    self.repeating_trucks = (['Batmobile'])

  def tearDown(self):
    print('teardown')

  def test_repeating_truck_check(self):
    self.assertEqual(dc.repeating_truck_check(self.cargo_options),
      (set(['Batmobile'])))

  def test_eliminate_duplicates(self):
    self.assertEqual(dc.eliminate_duplicates(self.best_options, self.cargo_options, self.repeating_trucks), ({
        'A': {'Alfredo': 5.79198868163568},
        'C': {'Alfredo': 25.335222757961162},
        'B': {'Batmobile': 6.409864033717816},
        'D': {'Banana Boat': 46.0}
      }))