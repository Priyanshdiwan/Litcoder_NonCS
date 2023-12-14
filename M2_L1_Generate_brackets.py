def parentheses(n):
    result = []
    
    def actual_generator(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        
        if left < n:
            actual_generator(s + '(', left + 1, right)
        
        if right < left:
            actual_generator(s + ')', left, right + 1)
    
    actual_generator('', 0, 0)
    output_string = '.'.join(result)
    return output_string

input_combination= int(input())
print(parentheses(input_combination))