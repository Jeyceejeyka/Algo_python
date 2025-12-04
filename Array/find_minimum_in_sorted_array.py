# Problem Statement: Find Minimum in Rotated Sorted Array

# You are given an array of unique integers that was originally sorted in ascending order, but then rotated at an unknown pivot index.

# Example of a rotated sorted array:

# Original sorted: [0,1,2,4,5,6,7]

# After rotation: [4,5,6,7,0,1,2]

# Your task is to find the minimum element in this array.

# Requirements

# The array has no duplicate elements.

# You must write an algorithm that runs in O(log n) time.

#  Input

# An integer array nums of length n, rotated at some pivot.

#  Output

# Return the minimum element in arr.
def find_minimum_in_rotated_sorted_array(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    
    return arr[left]



print(find_minimum_in_rotated_sorted_array([3,4,5,1,2])) 
print(find_minimum_in_rotated_sorted_array([4,5,6,7,0,1,2])) 
print(find_minimum_in_rotated_sorted_array([11,13,15,17]))  
#  Examples
#  Example 1

# Input:
# nums = [3,4,5,1,2]
# Output:
# 1

# Explanation: The array was rotated at index 3.

#  Example 2

# Input:
# nums = [4,5,6,7,0,1,2]
# Output:
# 0

#  Example 3

# Input:
# nums = [11,13,15,17]
# Output:
# 11
# Explanation: The array is not rotated.