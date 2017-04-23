import unittest

from math_fun import solve_me_first


class MathFunTestCases(unittest.TestCase):
    def test_correct_output(self):
        num1 = 5
        num2 = 5
        result = solve_me_first(num1, num2)
        self.assertEqual(result, 10)

    def test_wrong_output(self):
        num1 = 1
        num2 = 1
        result = solve_me_first(num1, num2)
        self.assertNotEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
