def min_max_sums(numbers):
    n = len(numbers)
    min_sum = float('inf')
    max_sum = float('-inf')
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    current_sum = numbers[i] + numbers[j] + numbers[k] + numbers[l]
                    min_sum = min(min_sum, current_sum)
                    max_sum = max(max_sum, current_sum)
    return min_sum, max_sum
input_numbers = list(map(int, input().split()))
min_sum, max_sum = min_max_sums(input_numbers)
print(min_sum, max_sum)