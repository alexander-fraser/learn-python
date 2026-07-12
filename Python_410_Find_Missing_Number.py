# Find the Missing Number
# Alexander Fraser
# 11 July 2026

import random

def setup():
    input_end = input("Creating a list of integers from 0 to n. n=")
    input_end = int(input_end)

    input_list = []
    for integer in range(0, input_end + 1):
        input_list.append(integer)

    input_missing = random.randint(0, input_end)
    input_list.pop(input_missing)

    return input_list

def find_missing_sum(input_list):
    list_sum = 0
    for integer in input_list:
        list_sum += integer

    list_length = len(input_list)
    full_sum = 0
    for integer in range(0, list_length + 1):
        full_sum += integer

    output_missing = full_sum - list_sum
    return output_missing
    
def find_missing_xor(input_list):
    test_list = []
    list_length = len(input_list)
    for integer in range(0, list_length + 1):
        test_list.append(integer)

    output_missing = list(set(test_list) ^ set(input_list))
    return output_missing

def main():
    print("Welcome to the 'find the missing number' program.")
    input_list = setup()
    print(input_list)
#    output_missing = find_missing_sum(input_list)
    output_missing = find_missing_xor(input_list)
    print(output_missing)

if __name__ == "__main__":
    main()
