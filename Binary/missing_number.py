# Missing Number
# Problem Statement

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Solution: Arithemtic Sum Formula
# We can find the missing number by calculating the expected sum of the first n natural numbers using
def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


print(missing_number([3, 0, 1]))  
print(missing_number([0, 1]))   
print(missing_number([9,6,4,2,3,5,7,0,1])) 


# Example 1

# Input:

# nums = [3, 0, 1]


# Output:

# 2


# Explanation:
# The numbers are in the range [0, 3].
# The number 2 is missing.

# Example 2

# Input:

# nums = [0, 1]


# Output:

# 2

# Example 3

# Input:

# nums = [9,6,4,2,3,5,7,0,1]


# Output:

# 8

# Constraints

# n == nums.length

# 1 ≤ n ≤ 10⁴

# 0 ≤ nums[i] ≤ n

# All numbers in nums are unique

# Follow-up

# Could you implement a solution using:

# O(n) time complexity

# O(1) extra space?