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

# Solution A: O(n³) (very slow)
def three_sum(nums):
    results = []
    nums = sorted(nums)
    
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) -1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    if triplet not in results:
                        results.append(triplet)
    return results

# soltion B: O(n²) much faster than above
def threeSum(arr):
    arr.sort()
    result = []
    
    for i in range(len(arr)):
        
        # skip duplicate values for i
        if i > 0 and arr[i] == arr[i - 1]:
            continue
    
        left = i + 1
        right = len(arr) - 1 
    
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([arr[i], arr[left], arr[right]])
                
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            
    return result

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))

print("-----")
    
        
print(three_sum([-1,0,1,2,-1,-4]))
print(three_sum([0,1,1]))
print(three_sum([0,0,0]))
# HOW THE ALGORITHM WORKS (In Words Only)
# Goal: Find all unique triplets in the array which gives the sum of zero.
# We use three nested loops to consider every possible triplet combination in the array.
# For each triplet, we check if the sum is zero.
# If it is, we add it to the results list if it's not already present to avoid duplicates.
# Finally, we return the list of unique triplets.   

    



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
