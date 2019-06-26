import unittest
import sys
sys.path.append('../app')
from calculate_distance import calculate_distance

class TestCalculateDistance(unittest.TestCase):
  def test_calculate_distance(self):
    self.assertEqual(calculate_distance(34, 9, 10, 2), 25)
    self.assertEqual(calculate_distance(1, 1, 5, 4), 5)
    self.assertEqual(calculate_distance(5, 4, 45, 13), 41)
    self.assertEqual(calculate_distance(5, 13.45, 12.345, 12.345), 7.427654407684838)
    self.assertEqual(calculate_distance(-5, -13.45, -12.345, -12.345), 7.427654407684838)
    self.assertEqual(calculate_distance(5, -13.45, 12.345, -12.345), 7.427654407684838)
    self.assertEqual(calculate_distance(5, -13.45, -12.345, -12.345), 17.38016254239298)

if __name__ == '__main__':
  unittest.main()