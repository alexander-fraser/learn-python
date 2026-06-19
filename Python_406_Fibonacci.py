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
    old_fib = 0
    new_fib = 1

    match requested_value:
        case 1:
            return old_fib
        case 2:
            return new_fib
        case _:
            pass

    for i in range(3, requested_value):
        calc_fib = old_fib + new_fib 
        old_fib = new_fib
        new_fib = calc_fib
    return calc_fib

def main():
    requested_value = collect_input()
    fib_value = calculate_fib(requested_value)
    print(fib_value)

if __name__ == "__main__":
    main()
