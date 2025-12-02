# LeetCode 152 — Maximum Product Subarray

# Problem Statement:

# Given an integer array nums, find a subarray (a contiguous non-empty sequence of elements) that has the largest product, and return the product.

# A subarray is a contiguous part of an array.

# ✔ Example 1

# Input:
# nums = [2,3,-2,4]
# Output:
# 6

def max_product_subarray(nums):
    if not nums:
        return 0

    max_product = float('-inf')
    current_product = nums[0]
    
    for value in range(len(nums)):
        if value == 0:
            current_product = nums[value]
        else:
            current_product *= nums[value]
        if current_product > max_product:
            max_product = current_product   
       
            
    return max_product

        # NB:Problem With this approach:
        #     # ---------------------------

        # Incorrect for arrays with negatives, because it only tracks the running product from the start.

        # Fails when a negative number can flip a minimum product to maximum.


# Correct Approach: Using Dynamic Programming
def max_product_subarray(nums):
    if not nums:
        return 0

    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product

        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])

        result = max(result, max_product)

    return result   


print(max_product_subarray([2,3,-2,4]))
print(max_product_subarray([-2,0,-1]))
print(max_product_subarray([-2,3,-4]))
print(max_product_subarray([2, -5, -2, -4]))
# Explanation:
# The subarray [2,3] has the maximum product of 6.

# ✔ Example 2

# Input:
# nums = [-2,0,-1]
# Output:
# 0

# Explanation:
# The result cannot be 2 because [-1 * -2] is not a contiguous subarray after the zero.

# 📌 Constraints

# 1 <= nums.length <= 2 * 10^4

# -10 <= nums[i] <= 10

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.