def longest_substring_even_vowels(s):
    vowels = set("aeiou")
    count_positions = {(0, 0, 0, 0, 0): -1}  
    counts = [0, 0, 0, 0, 0] 
    max_length = 0
    for i, char in enumerate(s):
        if char in vowels:
            index = vowels.index(char)
            counts[index] += 1
        key = tuple(counts)
        if key not in count_positions:
            count_positions[key] = i
        else:
            max_length = max(max_length, i - count_positions[key])
    return max_length
in_string=input()
print(longest_substring_even_vowels(in_string))