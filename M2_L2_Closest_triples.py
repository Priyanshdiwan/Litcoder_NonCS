def find_closest_Sum(nums, target):
    nums.sort()
    closest_sum = float('inf')

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum

            if current_sum < target:
                left += 1
            else:
                right -= 1

    return closest_sum



in_array = input().split(" ")
in_target=int(input())
processed_array=[int(ch) for ch in in_array]
print(find_closest_Sum(processed_array,in_target))