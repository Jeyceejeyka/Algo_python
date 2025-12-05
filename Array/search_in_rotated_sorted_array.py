# 🔍 Problem Statement: Search in Rotated Sorted Array

# You are given an integer array nums that was originally sorted in ascending order, but was rotated at an unknown pivot index.
# (For example, [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].)

# The array may contain distinct integers.

# You are also given an integer target.

# Your task is to return the index of the target if it exists in the rotated array.
# If the target is not found, return -1.

# Your algorithm must run in O(log n) time.

# Example 1

# Input:
# nums = [4,5,6,7,0,1,2], target = 0
# Output:
# 4

# Example 2

# Input:
# nums = [4,5,6,7,0,1,2], target = 3
# Output:
# -1

# Example 3

# Input:
# nums = [1], target = 0
# Output:
# -1

# Constraints

# 1 <= nums.length <= 5000

# -10⁴ <= nums[i] <= 10⁴

# All values in nums are unique

# nums is a rotated sorted array

# Your solution must run in O(log n)