# Two Sum
# Alexander Fraser
# 19 June 2026
# Given a list of integers, gives the two that add up to the target.

def collect_input():
    while True:
        try: 
            exit_code = False
            input_list = input("Enter list of integers separated by"
                + "spaces (blank uses default list): ")
            input_target = input("Target sum: ")
            input_target = int(input_target)
            if exit_code == True:
                break
        except:
            pass
    return input_list, input_target

def calculate_fib(input_target):
    fib_list = [0, 1]

    if input_target <= 2:
        return fib_list[input_target-1]

    for i in range(3, input_target+1):
        fib_list.append(fib_list[i-2] + fib_list[i-3])
    return fib_list, fib_list[input_target-1]

def main():
    input_target = collect_input()
    fib_list, fib_value = calculate_fib(input_target)
    print(fib_list)
    print(fib_value)

if __name__ == "__main__":
    main()
