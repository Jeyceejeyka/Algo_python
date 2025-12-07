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

# HOW THE ALGORITHM WORKS (In Words Only)
# Goal: Find all unique triplets in the array which gives the sum of zero.
# We use three nested loops to consider every possible triplet combination in the array.
# For each triplet, we check if the sum is zero.
# If it is, we add it to the results list if it's not already present to avoid duplicates.
# Finally, we return the list of unique triplets.   
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


# Given an array of integers, we want to find ALL unique triplets (3 numbers) that add up to zero.

# Example
# Input: [-1,0,1,2,-1,-4]
# Output:

# [[-1,-1,2], [-1,0,1]]

#  The core ideas
# ✔ Idea 1 — Sorting makes life easier

# We first sort the array, because when a list is sorted:

# equal values will be beside each other

# we can use pointers to move left/right logically

# detecting duplicates becomes simple

# Example sorted:

# [-4, -1, -1, 0, 1, 2]

# ✔ Idea 2 — Pick one number, then find 2 more numbers

# We fix one number arr[i]

# Then we search for 2 more numbers whose sum is -(arr[i])

# This is basically 2-sum AND 3-sum at the same time.

# ✔ Idea 3 — Use two pointers (left & right)

# After picking arr[i]:

# left pointer starts just after i

# right pointer starts at the end

#     i     L           R
# [-4, -1, -1, 0, 1, 2]


# Now we check:

# arr[i] + arr[left] + arr[right]

# ✔ Idea 4 — Compare the total with 0
# If sum < 0

# ➡ move left forward
# (we need bigger numbers)

# If sum > 0

# ➡ move right backward
# (we need smaller numbers)

# If sum == 0

#  we found a triplet!

# ✔ Idea 5 — Skip duplicates (VERY IMPORTANT)

# After finding one valid pair:

# If left points to another value that’s the same:

# skip it


# If right points to another value that’s the same:

# skip it


# This prevents repeated results.

#  Full solving strategy in simple words
# Sort the array
# For each number i:

#     If it's a duplicate → skip it

#     Put left pointer on next position
#     Put right pointer on last position

#     While left < right:
        
#         Calculate sum of three numbers

#         If sum is zero → add them to result
#         If sum is less than zero → move left
#         If sum is more than zero → move right
        
#         Skip duplicates of left and right

#  Why this works

# Sorting arranges numbers in order

# Two pointers allow us to adjust the sum efficiently

# Only unique triples remain

# Time complexity becomes O(n²) instead of O(n³)

# Triple loops = too slow
# Two pointers = efficient

#  Intuition to remember

# Here’s the mental model:

# Fix one number
# → Balance the remaining sum using two pointers
# → Move pointers based on whether the sum is too big or too small
# → Skip duplicates each time

# How someone understands this problem

# It becomes clear when you realize 3sum is basically:

# One number fixed + Two-sum problem

# Instead of checking ALL combinations we:

# keep order

# adjust sum intelligently

#  What you should take away
# Learn patterns:

# Sorting + two pointers shows up in MANY problems

# Duplicate skipping pattern is SUPER common

# Transforming a 3-sum into a 2-sum is the trick

# If you understand that flow — you can solve:

# 2 Sum

# 3 Sum

# 4 Sum

# K-Sum

# Two pointers questions

# Duplicate avoidance problems


print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))

print("-----")
    
        
print(three_sum([-1,0,1,2,-1,-4]))
print(three_sum([0,1,1]))
print(three_sum([0,0,0]))

    



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
