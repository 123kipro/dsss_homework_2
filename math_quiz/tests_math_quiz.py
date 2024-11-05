import unittest
from math_quiz import random_integer, random_operator, arithmetic_operation


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # Test if the random operator is one of the expected operators
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            operator = random_operator()
            self.assertIn(operator, operators)

    def test_arithmetic_operation(self):
        # Test the arithmetic operation function with different test cases
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (3, 1, '+', '3 + 1', 4),
            (3, 1, '-', '3 - 1', 2),
            (3, 1, '*', '3 * 1', 3),
            (9, 4, '+', '9 + 4', 13),
            (9, 4, '-', '9 - 4', 5),
            (9, 4, '*', '9 * 4', 36),
            (10, 8, '+', '10 + 8', 18),
            (10, 8, '-', '10 - 8', 2),
            (10, 8, '*', '10 * 8', 80),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = arithmetic_operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
