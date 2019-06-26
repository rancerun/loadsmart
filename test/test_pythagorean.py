import unittest
import sys
sys.path.append('../app')
from pythagorean import pythagorean

class TestPythagorean(unittest.TestCase):
  def test_pythagorean(self):
    self.assertEqual(pythagorean(3, 4), 5)
    self.assertEqual(pythagorean(-3, -4), 5)
    self.assertEqual(pythagorean(5.0, 12.0), 13)
    self.assertEqual(pythagorean(50.895, -62.234), 80.39509799110888)

if __name__ == '__main__':
  unittest.main()