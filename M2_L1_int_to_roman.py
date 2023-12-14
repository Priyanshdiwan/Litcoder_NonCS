def int_converter(string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    output = 0
    prev_value = 0

    for char in reversed(string):
        value = roman_dict[char]
        if value < prev_value:
            output -= value
        else:
            output += value
        prev_value = value

    return output

roman_numeral = input()
print(int_converter(roman_numeral))