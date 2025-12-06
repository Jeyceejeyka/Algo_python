# 3Sum — Problem Statement

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that

# i != j,
# i != k,
# and j != k


# and

# nums[i] + nums[j] + nums[k] == 0

# Notice:

# The solution set must not contain duplicate triplets.

# You may return the answer in any order.



# Example 1

# Input

# nums = [-1,0,1,2,-1,-4]


# Output

# [[-1,-1,2],[-1,0,1]]


# Explanation:

# The triplet [-1, -1, 2] sums to 0

# The triplet [-1, 0, 1] sums to 0

# Example 2

# Input

# nums = [0,1,1]


# Output

# []

#  Example 3

# Input

# nums = [0,0,0]


# Output

# [[0,0,0]]

#  Constraints
# 3 ≤ nums.length ≤ 3000
# -10^5 ≤ nums[i] ≤ 10^5
