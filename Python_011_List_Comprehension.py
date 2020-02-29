# List Comprehension
# Alexander Fraser
# 28 Febuary 2020

"""
Write one line of Python that takes a list and
makes a new list that has only the even elements in it.
"""


def main():
    integer_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    # A list comprehension for finding the even elements of a list.
    even_list = [x for x in integer_list if x % 2 == 0]
    print(even_list)


if __name__ == "__main__":
    main()