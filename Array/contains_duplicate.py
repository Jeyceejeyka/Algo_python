# 🟦 Contains Duplicate (LeetCode 217)
# 📘 Problem Statement

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# 🧪 Example 1

# Input:
# nums = [1,2,3,1]
# Output:
# true
# Explanation:
# 1 appears twice.

# 🧪 Example 2

# Input:
# nums = [1,2,3,4]
# Output:
# false
# Explanation:
# All elements are unique.

# complexity: O(n^2)
# def contains_duplicate(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] == arr[j]:
#                 return True
#     return False    

# complexity: O(n log n) due to sorting
# def contains_duplicate(arr):
#     arr.sort()
#     for i in range(len(arr)-1):
#         if arr[i] == arr[i+1]:
#             return True
#     return False

# complexity: O(n) using a set
def contains_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False


print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))
print(contains_duplicate([1,4,2]))


# 🧪 Example 3

# Input:
# nums = [1,1,1,3,3,4,3,2,4,2]
# Output:
# true

# 📌 Constraints

# 1 <= nums.length <= 10^5

# -10^9 <= nums[i] <= 10^9