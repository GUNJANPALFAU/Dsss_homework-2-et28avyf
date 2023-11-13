import unittest
from math_quiz import generate_random_integer, choose_random_operation, generate_math_problem, calculate_answer

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated a
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_random_operation(self):
        # Test if the chosen operation is one of the expected operations
        operations = set(['+', '-', '*'])
        for _ in range(1000):  # Test a large number of random values
            rand_op = choose_random_operation()
            self.assertIn(rand_op, operations)

    #def test_generate_math_problem(self):
    def test_generate_math_problem(self):
    # Test if generated math problems are in the expected format
     for _ in range(1000):  # Test a large number of random values
        num1, num2, operator = generate_math_problem()
        self.assertIsInstance(num1, int)
        self.assertIsInstance(num2, int)
        self.assertIn(operator, ['+', '-', '*'])
        pass

    def test_calculate_answer(self):
        # correctness of the calculate_answer function
        test_cases = [
            (5, 2, '+', 7),
            (8, 3, '-', 5),
            (4, 6, '*', 24),
        ]

        for num1, num2, operator, expected_answer in test_cases:
            calculated_answer = calculate_answer(num1, num2, operator)
            self.assertEqual(calculated_answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
