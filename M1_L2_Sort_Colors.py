def custom_sort(item):
    color_order = {'Crimson': 0, 'Ivory': 1, 'Azure': 2}
    if isinstance(item, int):
        return item
    elif isinstance(item, str):
        return color_order.get(item, float('inf'))
    else:
        raise ValueError("Invalid input type")
def sort_colors(nums):
    nums.sort(key=custom_sort)
    result_string = ' '.join(map(str, nums))
    return result_string
in_nums = input().split(" ")
nums=[int(ch) for ch in in_nums]
print(sort_colors(nums))