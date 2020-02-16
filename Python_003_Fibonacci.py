# Fibonacci
# Alexander Fraser
# 8 February 2020

# This program outputs all Fibonacci numbers up to the 
# integer specified by the user.

import Python_002_Primes as prime_script

def compute_fibonacci(limit_value):
    fib_list = [1]
    
    a = 0
    b = 1

    for _ in range(0, limit_value - 1):
        c = a + b
        a = b
        b = c
        
        fib_list.append(c)

    return fib_list

def main():
    print("This program will output all Fibonacci numbers up to the limit specified.")
    limit_value = prime_script.collect_stop_value()
    fib_list = compute_fibonacci(limit_value)
    print(fib_list)

if __name__ == "__main__":
    main()