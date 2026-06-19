# Fibonacci
# Alexander Fraser
# 19 June 2026
# Prints the requested value from the Fibonacci sequence.

def collect_input():
    while True:
        try: 
            requested_value = input("Print nth value from the Fibonacci sequence. n=")
            requested_value = int(requested_value)
            if requested_value > 0:
                break
        except:
            pass
    return requested_value

def calculate_fib(requested_value):
    fib_list = [0, 1]

    if requested_value <= 2:
        return fib_list[requested_value-1]

    for i in range(3, requested_value+1):
        fib_list.append(fib_list[i-2] + fib_list[i-3])
    return fib_list, fib_list[requested_value-1]

def main():
    requested_value = collect_input()
    fib_list, fib_value = calculate_fib(requested_value)
    print(fib_list)
    print(fib_value)

if __name__ == "__main__":
    main()
