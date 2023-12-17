def page_turns(n, p):
    turns_from_front = p // 2
    turns_from_back = (n // 2) - (p // 2)
    return min(turns_from_front, turns_from_back)
n = int(input())
p = int(input())
result = page_turns(n, p)
print(result)
               