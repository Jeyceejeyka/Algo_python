# Two Sum — Problem Statement

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# solution 1: with time complexity O(n^2)

# NOTE:
#     enumerate(nums) returns pairs like:
#     (index, value)

def two_sum(nums, target):
    two_numbers = []
    
    for i in enumerate(nums):
        for j in enumerate(nums):
            if i[0] != j[0]:
                if i[1] + j[1] == target:
                    two_numbers.append(i[0])
                    two_numbers.append(j[0])
                    return two_numbers
    return two_numbers

print(two_sum([2, 7, 11, 15], 9))  
print(two_sum([3, 2, 4], 6))       
print(two_sum([3, 3], 6))        
print("\n")

# solution 1 better approach:
def two_sum_better_approach(nums, target):
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if i != j and num1 + num2 == target:
                return [i, j]
    return []
  
  
print(two_sum_better_approach([2, 7, 11, 15], 9))  
print(two_sum_better_approach([3, 2, 4], 6))       
print(two_sum_better_approach([3, 3], 6))
print("\n")



# solution 2: with time complexity O(n)
def two_sum2(nums, target):
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return []

print(two_sum2([2, 7, 11, 15], 9))  
print(two_sum2([3, 2, 4], 6))       
print(two_sum2([3, 3], 6))

# Example 1:

# Input:
# nums = [2, 7, 11, 15], target = 9
# Output:
# [0, 1]
# Explanation:
# nums[0] + nums[1] = 2 + 7 = 9.

# Example 2:

# Input:
# nums = [3, 2, 4], target = 6
# Output:
# [1, 2]

# Example 3:

# Input:
# nums = [3, 3], target = 6
# Output:
# [0, 1]

# Constraints:

# 2 <= nums.length <= 10^4

# -10^9 <= nums[i] <= 10^9

# -10^9 <= target <= 10^9

# Exactly one valid answer exists


