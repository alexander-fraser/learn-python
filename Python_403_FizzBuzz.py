# FizzBuzz
# Alexander Fraser
# 28 May 2026

def collect_input():
    size_str = input("Pick an ending number: ")
    size = int(size_str)
    return size

def create_list(size):
    input_list = []
    for value in range(1, size+1):
        input_list.append(value)
    return input_list

def determine_fizzbuzz(value):
   match value:
        case x if (x % 3 == 0) & (x % 5 == 0):
            return "fizzbuzz"
        case x if x % 3 == 0:
            return "fizz"
        case x if x % 5 == 0:
            return "buzz"
        case _:
            return str(value)

def process_output(input_list):
    output_list = map(determine_fizzbuzz, input_list)
    return output_list

def main():
    size = collect_input()
    input_list = create_list(size)
    print(list(input_list))
    output_list = process_output(input_list)
    print(list(output_list))

if __name__ == "__main__":
    main()
