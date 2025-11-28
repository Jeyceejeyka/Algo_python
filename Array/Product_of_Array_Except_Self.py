# Problem: Product of Array Except Self

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
    
    
#  Why this algorithm is smart
# ------------------------------------------------

# Instead of multiplying all elements except i inside a loop (which would be O(n²)), this method:

# builds left products in one pass

# builds right products in another pass

# multiplies them together

# uses O(1) extra space (only prefix & suffix variables)

# Total time: O(n)
# Total extra space: O(1)
    
    
    
# 1. Brute Force (Very Slow — O(n²))
#  Idea

# For each index, multiply all other elements.

#  Inefficient

# Will time out for large arrays.

# Code
def product_except_self_bruteforce(nums):
    n = len(nums)
    answer = []

    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= nums[j]
        answer.append(prod)

    return answer

# Complexity

# Time: O(n²)

# Space: O(1) extra

#  2. Using Division (NOT allowed in LeetCode)

# Only works if no zeros are in the array.

# Code
# def product_except_self_div(nums):
#     total_product = 1
#     zero_count = nums.count(0)

#     if zero_count > 1:
#         return [0] * len(nums)

#     for num in nums:
#         if num != 0:
#             total_product *= num

#     answer = []
#     for num in nums:
#         if num == 0:
#             answer.append(total_product)
#         else:
#             answer.append(total_product // num if zero_count == 0 else 0)

#     return answer

# Complexity

# Time: O(n)

# Space: O(1) extra

# BUT: Not allowed because division is banned.
    

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