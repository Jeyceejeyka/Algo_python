# Problem: Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) that has the largest sum, and return its sum.

# 🔹 Solution using Kadane's Algorithm  : 
# ----------------------------------------- 
            
def max_subarray(nums):   
    
    max_num = nums[0]
    current_sum = 0
    
    
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_num = max(max_num, current_sum)
        
        
    return max_num

    
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6    
print(max_subarray([1]))                    # Output: 1
print(max_subarray([5,4,-1,7,8]))           # Output: 23




# Example 1

# Input:
# nums = [-2,1,-3,4,-1,2,1,-5,4]

# Output:
# 6

# Explanation:
# The subarray [4, -1, 2, 1] has the largest sum = 6.

# Example 2

# Input:
# nums = [1]

# Output:
# 1

# Example 3

# Input:
# nums = [5,4,-1,7,8]

# Output:
# 23

# Constraints

# 1 ≤ nums.length ≤ 10^5

# -10^4 ≤ nums[i] ≤ 10^4