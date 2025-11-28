# 🟦 Problem: Product of Array Except Self

# Given an integer array nums, return an array answer such that:

# answer[i] = product of all the elements of nums except nums[i]

# You must solve it without using division, and the solution must run in:

# Time Complexity: O(n)

# Space Complexity: O(1) extra space (the output array does not count as extra space).

def product_of_array_except_self(arr):
    n = len(arr)
    answer = [1] * n
    
    # Calculate left products
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= arr[i]
    
    # Calculate right products and multiply with left products
    right_product = 1
    for i in range(n-1, -1, -1):
        answer[i] *= right_product
        right_product *= arr[i]
    
    return answer
print(product_of_array_except_self([1,2,3,4]))  # Output: [24,12,8,6]
print(product_of_array_except_self([-1,1,0,-3,3]))  # Output: [0,0,9,0,0]
    

# Example 1

# Input:
# nums = [1, 2, 3, 4]

# Output:
# [24, 12, 8, 6]

# Example 2

# Input:
# nums = [-1, 1, 0, -3, 3]

# Output:
# [0, 0, 9, 0, 0]

# Constraints

# 2 ≤ nums.length ≤ 10⁵

# −30 ≤ nums[i] ≤ 30

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.