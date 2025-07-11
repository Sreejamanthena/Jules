import unittest
from unittest.mock import patch
import io
import sys

# It's good practice to be able to import the module you're testing.
# To do this, we might need to adjust the Python path if solve.py is not in the same directory
# or if it's not structured as a package. For this simple case, direct import might work
# if they are in the same directory. Otherwise, more complex path manipulation might be needed.
# Assuming solve.py is in the same directory for simplicity here.
from solve import solve

class TestSolve(unittest.TestCase):

    def run_test_case(self, input_data, expected_output):
        """Helper function to run a test case with given input and expected output."""
        # Redirect stdin and stdout
        original_stdin = sys.stdin
        original_stdout = sys.stdout
        sys.stdin = io.StringIO(input_data)
        sys.stdout = io.StringIO()

        solve()  # Call the main function from solve.py

        # Get the output
        output = sys.stdout.getvalue().strip()

        # Restore stdin and stdout
        sys.stdin = original_stdin
        sys.stdout = original_stdout

        self.assertEqual(output, expected_output)

    def test_sample_case(self):
        input_data = "3 2\n3 2 -1 4\n0 1"
        expected_output = "3 2"
        self.run_test_case(input_data, expected_output)

    def test_all_elements_query(self):
        input_data = "5 1\n10 20 5 30 15\n4"
        expected_output = "5"
        self.run_test_case(input_data, expected_output)

    def test_single_element_array(self):
        input_data = "1 1\n100\n0"
        expected_output = "100"
        self.run_test_case(input_data, expected_output)

    def test_multiple_queries_same_min(self):
        input_data = "4 3\n5 2 8 1\n1 2 3" # min up to index 1 is 2, up to 2 is 2, up to 3 is 1
        expected_output = "2 2 1"
        self.run_test_case(input_data, expected_output)

    def test_negative_numbers(self):
        input_data = "5 3\n-1 -5 0 -10 2\n1 3 4" # min up to 1 is -5, up to 3 is -10, up to 4 is -10
        expected_output = "-5 -10 -10"
        self.run_test_case(input_data, expected_output)

    def test_query_index_zero(self):
        input_data = "3 2\n10 1 5\n0 0"
        expected_output = "10 10"
        self.run_test_case(input_data, expected_output)

if __name__ == '__main__':
    unittest.main()
