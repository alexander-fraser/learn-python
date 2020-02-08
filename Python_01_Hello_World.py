# Hello World
# Alexander Fraser
# 8 February 2020

def collect_name():
    user_input = input("What is your name?\n")
    return user_input

def parse_input(user_input):
    user_name = user_input.upper()
    return user_name

def print_greeting(user_name):
    print("Hello, {0}".format(user_name))

def main():
    print("\nHello World!")
    print("I have become self-aware.")
    user_input = collect_name()
    user_name = parse_input(user_input)
    print_greeting(user_name)

if __name__ == "__main__":
    main()
