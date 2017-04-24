import unittest

from math_fun import Calculator


class MathFunTestCases(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_solve_me_first_returns_correct_result(self):
        result = self.calc.solve_me_first(2, 2)
        self.assertEqual(result, 4)

    def test_solve_me_first_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.solve_me_first, 'two', 'three')

    def test_solve_me_first_returns_error_message_if_a_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.solve_me_first, 2, 'three')

    def test_solve_me_first_returns_error_message_if_b_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.solve_me_first, 'two', 3)


if __name__ == "__main__":
    unittest.main()
