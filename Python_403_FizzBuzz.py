# FizzBuzz
# Alexander Fraser
# 28 May 2026

def collect_input():
    size_str = input("Pick an ending number: ")
    size = int(size_str)
    return size

def determine_fizzbuzz(value):
    fizz = 0
    buzz = 0
    fizzbuzz = 0

    if value % 3 == 0:
        fizz = 1
    if value % 5 == 0:
        buzz = 1
    if (fizz == 1 & buzz == 1):
        fizzbuzz = 1

    if fizzbuzz == 1:
        return "fizzbuzz"
    elif fizz == 1:
        return "fizz"
    elif buzz == 1:
        return "buzz"
    else:
        return str(value)

def main():
    size = collect_input()
    for value in range(0, size+1):
        output_text = determine_fizzbuzz(value)
        print(output_text)

if __name__ == "__main__":
    main()
