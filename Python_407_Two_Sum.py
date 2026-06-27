# Two Sum
# Alexander Fraser
# 19 June 2026
# Given a list of integers, gives the two that add up to the target.

def collect_input():
    retry_message = False
    while True:
        if retry_message == True:
            print("Invalid input. Please try again.")
        retry_message = True

        try: 
            input_valid = True

            input_string = input(
                "Enter list of positive integers separated by spaces (blank "
                "uses default list): "
            )
            input_list = input_string.split()
            for index, value in enumerate(input_list):
                value = int(value)
                if value <= 0:
                   input_valid = False 
                input_list[index] = value

            input_target = input("Target sum: ")
            input_target = int(input_target)
            if input_target <= 0:
               input_valid = False 

            if input_valid == True:
                break
        except:
            pass

    return input_list, input_target

def calculate_sum(input_list, input_target):
    for first_value in input_list:
        for second_value in input_list:
            if (first_value + second_value) == input_target:
                return [first_value, second_value]
    return "Unable to find sum."

def main():
    input_list, input_target = collect_input()
    if input_list == []:
        input_list = [1, 2, 3, 5, 7, 11, 15]
    output_list = calculate_sum(input_list, input_target)
    print("Input list: ", input_list)
    print("Target: ", input_target)
    print("Addends: ", output_list)

if __name__ == "__main__":
    main()
