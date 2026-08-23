# 0002 Add Two Numbers
# Alexander Fraser
# 22 August 2026

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

def add_two_numbers(l1: list[int], l2: list[int]) -> list[int]:
    """Take two integers stored in inverted lists. 
    Return the sum of the two integers as an inverted list."""
    input_lists = [l1, l2]
    input_integers = []
    
    for item in input_lists:
        string = ""
        for digit in reversed(item):
            string = string + str(digit)
        input_integers.append(int(string))

    sum_integer = input_integers[0] + input_integers[1]
    sum_string = str(sum_integer)
    sum_list = []
    for digit in reversed(sum_string):
        sum_list.append(int(digit))

    return sum_list

def test_script() -> None:
    """Test the function on a set of predefined test cases."""
    test_cases = [
        {"l1": [2,4,3], "l2": [5,6,4], "output": [7,0,8]},   
        {"l1": [0], "l2": [0], "output": [0]},   
        {"l1": [9,9,9,9,9,9,9], "l2": [9,9,9,9], "output": [8,9,9,9,0,0,0,1]},   
    ]
    
    for index, test in enumerate(test_cases):
        result = add_two_numbers(test["l1"], test["l2"])
        assert result == test["output"], (
            f"Test {index} failed. Expected: {test["output"]}. Realized: {result}."
        )
        print(f"Test {index} passed.")

def main() -> None:
    test_script()

if __name__ == "__main__":
    main()
