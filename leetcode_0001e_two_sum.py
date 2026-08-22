# 0001 Two Sum
# Alexander Fraser
# 2 August 2026

"""
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    """Return the indices of two numbers whose sum equals the target."""
    past_differences = {}

    for index, value in enumerate(nums):
        if value in past_differences:
            return [past_differences[value], index]
        else:
            difference = target - value           
            past_differences[difference] = index

    raise ValueError("No two numbers sum to the target.")

def test_script() -> None:
    """Test the function on a set of predefined test cases."""
    test_cases = [
        {"nums": [2,7,11,15], "target": 9, "output": [0,1]},   
        {"nums": [3,2,4], "target": 6, "output": [1,2]},   
        {"nums": [3,3], "target": 6, "output": [0,1]},   
    ]
    
    for index, test in enumerate(test_cases):
        result = two_sum(test["nums"], test["target"])
        assert result == test["output"], (
            f"Test {index} failed. Expected: {test["output"]}. Realized: {result}."
        )
        print(f"Test {index} passed.")

def main() -> None:
    test_script()

if __name__ == "__main__":
    main()
