import sys
import os
import unittest
sys.path.append(os.path.abspath('../app'))
import app.duplicates_check as dc

class TestDuplicatesCheck(unittest.TestCase):
  def setUp(self):
    print('setup')
    self.cargo_options = {
      'A': [{'Batmobile': 17.757531886594617}, {'Alfredo': 18.390497377276045}],
      'C': [{'Batmobile': 6.981600672073832}, {'Alfredo': 25.335222757961162}],
      'B': [{'Slam Dunk': 90.64425911395827}, {'Zebra Stripes': 130.15019508740355}],
      'D': [{'Banana Boat': 46.0}, {'Caramel Swirls': 52.031417601311496}]}
    self.best_options = {
      'B': {'Slam Dunk': 90.64425911395827},
      'D': {'Banana Boat': 46.0}}
    self.repeating_trucks = (['Batmobile'])

  def tearDown(self):
    print('teardown')

  def test_repeating_truck_check(self):
    self.assertEqual(dc.repeating_truck_check(self.cargo_options),
      (set(['Batmobile'])))

  def test_eliminate_duplicates(self):
    self.assertEqual(dc.eliminate_duplicates(self.best_options, self.cargo_options, self.repeating_trucks), ({
        'A': {'Alfredo': 18.390497377276045},
        'B': {'Slam Dunk': 90.64425911395827},
        'C': {'Batmobile': 6.981600672073832},
        'D': {'Banana Boat': 46.0}
      }))