# Roman to Integer
# Alexander Fraser
# 28 June 2026
# Convert roman numerals to an integer.

roman_numerals = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def input_roman_numeral():
    retry_message = False
    while True:
        if retry_message == True:
            print("Invalid input. Please try again.")
        retry_message = True

        try: 
            input_valid = True
            input_roman = input("Enter a value in roman numerals:")
            for character in input_roman:
                if character not in roman_numerals:
                    input_valid = False

            if input_valid == True:
                break
        except:
            pass

    if input_roman == "":
        return "MCMXCIV"
    return input_roman

def convert_roman(input_roman):
    output_integer = 0
    for index, numeral in enumerate(input_roman):
        current_value = roman_numerals[numeral]

        if index + 1 < len(input_roman):
            next_value = roman_numerals[input_roman[index+1]]
        else:
            next_value = 0

        if current_value < next_value:
            output_integer -= current_value
        else:
            output_integer += current_value

    return output_integer

def main():
    input_roman = input_roman_numeral()
    output_integer = convert_roman(input_roman)
    print(output_integer)

if __name__ == "__main__":
    main()
