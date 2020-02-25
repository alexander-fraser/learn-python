# List Overlap
# Alexander Fraser
# 24 Febuary 2020

"""
Requirements:
- random

Write a program that returns a list that contains only
the elements that are common between the lists
(without duplicates). Make sure your program works on two
lists of different sizes.
"""

from random import randint

def generate_random_list():
    # Generates a list of random length (1-20 elements) of integers (1-9).
    input_list = []
    list_length = randint(1,20)

    for _ in range(0, list_length):
        input_list.append(randint(1,10))

    return input_list

def compare_lists(list1, list2):
    # Outputs a list of the elements common between the two input lists.
    output_list = []

    for element in list1:
        if (element in list2) and (element not in output_list):
            output_list.append(element)

    output_list = sorted(output_list)
    return output_list

def main():
    # Generates two lists of random length and with random integers.
    # Then outputs the elements that are common between the two lists.
    list1 = generate_random_list()
    list2 = generate_random_list()
    output_list = compare_lists(list1, list2)
    print(list1, "\n", list2, "\n", output_list)

if __name__ == "__main__":
    main()