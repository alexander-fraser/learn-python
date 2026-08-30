# 0003 Longest Substring without Repeating Characters
# Alexander Fraser
# 23 August 2026

"""
Given a string s, find the length of the longest substring without duplicate characters.
"""

def length_of_longest_substring(s: str) -> int:
    """Return the length of the longest substring without repeating characters."""
    string_list = []
    substring_list = []

    for character in s:
        if character in substring_list:
            string_list.append(substring_list.copy())
            substring_list.clear()
        substring_list.append(character)        
    string_list.append(substring_list.copy())   

    max_length = 0
    for substring_list in string_list:
        max_length = max(max_length, len(substring_list))
    return max_length

def test_script() -> None:
    """Test the function on a set of predefined test cases."""
    test_cases = [
        {"s": "abcabcbb", "output": 3},   
        {"s": "bbbbb", "output": 1},   
        {"s": "pwwkew", "output": 3},   
    ]
    
    for index, test in enumerate(test_cases):
        result = length_of_longest_substring(test["s"])
        assert result == test["output"], (
            f"Test {index} failed. Expected: {test["output"]}. Realized: {result}."
        )
        print(f"Test {index} passed.")

def main() -> None:
    test_script()

if __name__ == "__main__":
    main()
