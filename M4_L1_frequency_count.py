def frequency_count(arr):
    arr.sort()
    freq_dict = {}
    for num in arr:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    for key in range(max(arr) + 1):
        print(freq_dict.get(key, 0), end=" ")
if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input("").split()))
    frequency_count(array)