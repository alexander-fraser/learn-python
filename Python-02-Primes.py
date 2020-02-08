# Primes
# Alexander Fraser
# 8 Febuary 2020

# This program outputs all the prime numbers up to the 
# integer specified by the user.

def collect_stop_value():
    # This function prompts the user for an integer.
    # It loops until an integer is entered by the user.
    while True:
        try:
            user_input = input("What upper limit would you like to set?\n")
            limit_value = int(user_input)
        except:
            print("That was not a valid integer. Please try again.")

        else:
            if limit_value >= 2:
                break
            print("The integer entered was less than 2. Please try again.")

    return limit_value

def determine_prime(candidate_value):
    for i in range(2, candidate_value):
        if (candidate_value % i) == 0:
            return False

    return True

def loop_through_candidates(limit_value):
    primes_list = []
    
    for i in range(2, limit_value + 1):
        is_prime = determine_prime(i)

        if is_prime == True:
            primes_list.append(i)

    return primes_list

def main():
    print("This program will output all primes up to the number specified.")
    limit_value = collect_stop_value()
    primes_list = loop_through_candidates(limit_value)
    print(primes_list)

if __name__ == "__main__":
    main()