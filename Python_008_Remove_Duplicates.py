# Remove Duplicates
# Alexander Fraser
# 24 Febuary 2020

"""
Requirements:
- Python_007_List_Overlap

Write a program that takes two lists and returns a new list that 
contains all the elements of both without duplicates.
"""

from Python_007_List_Overlap import generate_random_list

def remove_duplicates(list1, list2):
    # Combines the two lists and uses the "set" function to remove duplicates. 
    combined_list = list1 + list2
    
    list_set = set(combined_list)
    output_list = list(list_set)
    
    output_list = sorted(output_list)
    return output_list

def main():
    # Generates two lists of random length and with random integers.
    # Then outputs the elements that are common between the two lists.
    list1 = generate_random_list()
    list2 = generate_random_list()
    output_list = remove_duplicates(list1, list2)
    print(list1, "\n", list2, "\n", output_list)

if __name__ == "__main__":
    main()