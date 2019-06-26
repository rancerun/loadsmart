import unittest
import sys
sys.path.append('../app/')
import calculations as cal

class TestCalculations(unittest.TestCase):
  def test_pythagorean(self):
    self.assertEqual(cal.pythagorean(3, 4), 5)
    self.assertEqual(cal.pythagorean(-3, -4), 5)
    self.assertEqual(cal.pythagorean(5.0, 12.0), 13)
    self.assertEqual(cal.pythagorean(50.895, -62.234), 80.39509799110888)

  def test_calculate_distance(self):
    self.assertEqual(cal.calculate_distance(34, 9, 10, 2), 25)
    self.assertEqual(cal.calculate_distance(1, 1, 5, 4), 5)
    self.assertEqual(cal.calculate_distance(5, 4, 45, 13), 41)
    self.assertEqual(cal.calculate_distance(5, 13.45, 12.345, 12.345), 7.427654407684838)
    self.assertEqual(cal.calculate_distance(-5, -13.45, -12.345, -12.345), 7.427654407684838)
    self.assertEqual(cal.calculate_distance(5, -13.45, 12.345, -12.345), 7.427654407684838)
    self.assertEqual(cal.calculate_distance(5, -13.45, -12.345, -12.345), 17.38016254239298)