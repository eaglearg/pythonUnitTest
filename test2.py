import unittest
import main

class TestMain(unittest.TestCase):
  def test_guess_function_wrong(self):
    guess=3 
    answer=6
    result = main.guess_function(guess, answer)
    self.assertFalse(result)

  def test_guess_function_true(self):
    guess=6 
    answer=6
    result = main.guess_function(guess, answer)
    self.assertTrue(result)

  def test_guess_function_out_range(self):
    guess=15
    answer=6
    result = main.guess_function(guess, answer)
    self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()