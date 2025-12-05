# 🔍 Problem Statement: Search in Rotated Sorted Array

# You are given an integer array nums that was originally sorted in ascending order, but was rotated at an unknown pivot index.
# (For example, [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].)

# The array may contain distinct integers.

# You are also given an integer target.

# Your task is to return the index of the target if it exists in the rotated array.
# If the target is not found, return -1.

# Your algorithm must run in O(log n) time.


def search_in_rotated_sorted_array(nums, target):
        
    left, right = nums[0], len(nums) - 1   
    
    while left <= right:            
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

print(search_in_rotated_sorted_array([4,5,6,7,0,1,2], 0))  
print(search_in_rotated_sorted_array([4,5,6,7,0,1,2], 3))

# HOW THE ALGORITHM WORKS (In Words Only)

# Goal: Find target inside a rotated sorted array in O(log n).

# We always track three positions:

# left → start of search range

# right → end of search range

# mid → middle of the range

# At each step we do this:

#  STEP-BY-STEP LOGIC
# Step 1 — Compute the middle

# mid = (left + right) // 2

# Check if nums[mid] is the target.

# If yes → return mid immediately.

# Step 2 — Determine which side is sorted

# One side will ALWAYS be normally sorted, even after rotation.

# We check:

# If nums[left] ≤ nums[mid] → Left side is sorted
# Otherwise → Right side is sorted.

# Step 3 — Decide which half to search
# ✔ CASE A — Left half is sorted

# This means numbers go in normal increasing order from left → mid.

# We now check:

# If target is inside that left range
# (nums[left] ≤ target < nums[mid])
# → Then search ONLY LEFT, so move right = mid - 1

# Else
# → Target must be on the RIGHT, so move left = mid + 1

# ✔ CASE B — Right half is sorted

# This means numbers go in normal increasing order from mid → right.

# Check:

# If target is inside that right range
# (nums[mid] < target ≤ nums[right])
# → Search RIGHT, so left = mid + 1

# Else
# → Target is on the LEFT, so right = mid - 1

# Step 4 — Shrink the search range

# Keep repeating:

# recompute mid

# decide sorted half

# eliminate one side

# Until:

# You find the target, or

# left passes right → return -1

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