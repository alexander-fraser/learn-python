# Divisors
# Alexander Fraser
# 24 Febuary 2020

"""
Requirements:
- Python_005_Odd_or_Even

Create a program that asks the user for a number and then
prints out a list of all the divisors of that number.
"""

from Python_005_Odd_or_Even import collect_integer

def identify_divisors(input_number):
    divisors_list = []

    for x in range(2, input_number):
        if input_number % x == 0:
            divisors_list.append(x)

    return divisors_list

def output_divisors(divisors_list):
    if len(divisors_list) == 0:
        print("It is prime.")
    else:
        print("The divisors of that number are: \n", divisors_list)

def main():
    input_number = collect_integer("Pick a random number: ", 0, 1000000)
    divisors_list = identify_divisors(input_number)
    output_divisors(divisors_list)

if __name__ == "__main__":
    main()