def reverse_string(input_str):
    chars = list(input_str)
    start, end = 0, len(chars) - 1

    while start < end:
        while start < end and not chars[start].isalpha(): start += 1
        while start < end and not chars[end].isalpha(): end -= 1
        chars[start], chars[end] = chars[end], chars[start]
        start, end = start + 1, end - 1

    return ''.join(chars)
    
string=str(input())
print(reverse_string(string))