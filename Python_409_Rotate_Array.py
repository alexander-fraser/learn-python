# Rotate Array
# Alexander Fraser
# 28 June 2026
# Shift elements in an array k places to the right.

default_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def collect_input():
    retry_message = False
    while True:
        if retry_message == True:
            print("Invalid input. Please try again.")
        retry_message = True

        try: 
            input_valid = True

            input_string = input(
                "Enter an array of items separated by commas (blank "
                "uses default array): "
            )
            input_list = [item.strip() for item in input_string.split(",")]

            input_shift = input("Shift array right by k places: ")
            input_shift = int(input_shift)
            if input_shift < 0:
               input_valid = False 

            if input_valid == True:
                break
        except:
            pass

    if input_string == "":
        input_list = default_array
    return input_list, input_shift

def shift_array(input_list, input_shift):
    output_list = []
    for output_index in range(0, len(input_list)):
        if output_index + input_shift < len(input_list):
            output_list.append(input_list[output_index + input_shift])
        else:
            output_list.append(input_list[output_index + input_shift - len(input_list)])
    return output_list

def main():
    input_list, input_shift = collect_input()
    output_list = shift_array(input_list, input_shift)
    print(output_list)

if __name__ == "__main__":
    main()
