def can_reach_end(nums):
    n = len(nums)
    max_reach = 0
    for i in range(n):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= n - 1:
            return True
    return False
nums = input().split(" ")
processed_nums=[int(ch) for ch in nums]
result = can_reach_end(processed_nums)
print(result)