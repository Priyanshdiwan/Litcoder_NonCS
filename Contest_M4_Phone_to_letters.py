def letter_combinations(digits):
    if not digits:
        return []
    digit_mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    def generate_combinations(index, current):
        if index == len(digits):
            combinations.append(current)
            return
        if digits[index] == '1':
            generate_combinations(index + 1, current)
        else:
            for letter in digit_mapping[digits[index]]:
                generate_combinations(index + 1, current + letter)
    combinations = []
    generate_combinations(0, '')
    return ' '.join(combinations)
in_digit=input()
print(letter_combinations(in_digit))
                                                                                                                            