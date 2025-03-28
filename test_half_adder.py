# import pytest
# import logging
# from half_adder import*
#
# logging.basicConfig(filename='test_results.log', level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s')
#
#
# @pytest.mark.parametrize("a,b,expected1,expected2", [
#     (False, False, False, False),
#     (False, True, True, False),
#     (True, False, True, False),
#     (True, True, False, True)
# ])
# def test_half_adder(a, b, expected1, expected2):
#     result1, result2 = half_adder(a, b)
#     logging.info(f"Testing half_adder with inputs a={a}, b={b}")
#     logging.info(f"Expected result: ({expected1}, {expected2}), Got result: ({result1}, {result2})")
#     assert half_adder(a, b) == (expected1, expected2)




import pytest
from half_adder import *


# Fixture to handle log file opening and closing
@pytest.fixture(scope="module")
def log_file():
    # Open the log file at the start of the test session
    file = open('test_output.log', 'w')
    # Write a header to the log file
    file.write("Test results:\n")
    file.write("=====================\n")
    yield file  # Yield the file to the test functions
    # Close the log file after the tests are finished
    file.close()


@pytest.mark.parametrize("a,b,expected1,expected2", [
    (False, False, False, False),
    (False, True, True, False),
    (True, False, True, False),
    (True, True, False, True)
])
def test_half_adder(a, b, expected1, expected2, log_file):
    result1, result2 = half_adder(a, b)

    # Write the test inputs and results to the log file
    log_file.write(f'Test inputs: a={a}, b={b} => expected1={expected1}, expected2={expected2}\n')
    log_file.write(f'Results: result1={result1}, result2={result2}\n')

    assert (result1, result2) == (expected1, expected2)
    log_file.write("Test passed\n\n")
