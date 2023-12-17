def find_unique_elements(arr):
    frequency_dict = {}
    for num in arr:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    unique_elements = sorted([key for key, value in frequency_dict.items() if value == 1])
    print(*unique_elements)
len_Arr=int(input())
input_arr =input().split(" ")
find_unique_elements(input_arr)