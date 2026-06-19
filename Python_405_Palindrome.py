# Palindrome
# Alexander Fraser
# 19 June 2026

def collect_input():
    return input("Enter phrase:")

def parse_phrase(unparsed_phrase):
    parsed_phrase = ""
    for character in unparsed_phrase:
        if character.isalpha() == True:
            parsed_phrase += character
    parsed_phrase = parsed_phrase.lower()
    return parsed_phrase

def check_palindrome(parsed_phrase):
    phrase_length = len(parsed_phrase)
    phrase_midpoint = phrase_length // 2
    for i in range(0, phrase_midpoint):
        if parsed_phrase[i] != parsed_phrase[phrase_length - 1 - i]:
            return False
    return True

def main():
    unparsed_phrase = collect_input()
    parsed_phrase = parse_phrase(unparsed_phrase)
    palindrome_result = check_palindrome(parsed_phrase)
    print(palindrome_result)

if __name__ == "__main__":
    main()
