def tower_breakers(num_tower, height_tower):
    if num_tower == 1:
        return 1
    if height_tower == 1:
        return 1
    if height_tower % 2 == 0:
        return 2
    return 1
num_tower,height_tower = map(int, input().split())
result = tower_breakers(num_tower, height_tower)
print(result)
                                                                                                                            