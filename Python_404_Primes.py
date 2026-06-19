# Primes
# Alexander Fraser
# 15 June 2026
# Generates all primes up to the value entered.

def collect_input():
    while True:
        try: 
            end_value = input("Print primes up to what value: ")
            end_value = int(end_value)
            if end_value > 0:
                break
        except:
            pass
    return end_value

def calculate_primes(end_value):
    prime_list = []
    for prime_candidate in range(2,end_value):
        if check_prime(prime_candidate) == True:
            prime_list.append(prime_candidate)
    return prime_list

def check_prime(prime_candidate):
    prime_indicator = True
    for factor in range(2,prime_candidate):
        if (prime_candidate % factor) == 0:
            prime_indicator = False 
    return prime_indicator

def main():
    end_value = collect_input()
    prime_list = calculate_primes(end_value)
    print(prime_list)

if __name__ == "__main__":
    main()
