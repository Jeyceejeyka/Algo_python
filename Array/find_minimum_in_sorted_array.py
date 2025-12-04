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

# Steps for Finding the Minimum in a Rotated Sorted Array (Binary Search Method)
# ----------------------------------------------------------------------------------------

# Start with two pointers:

# left = 0

# right = last index of the array

# If the first element is less than the last element, the array is not rotated.
# → The minimum is the first element. Stop.

# While left is less than right, repeat:

# Calculate the middle index:
# mid = (left + right) // 2

# Compare the middle element with the rightmost element.

# If the middle element is greater than the rightmost element:
# → The minimum is in the right half of the array.
# → Move left to mid + 1.

# Otherwise (middle element is less than or equal to the rightmost element):
# → The minimum is in the left half, including mid.
# → Move right to mid.

# Continue narrowing the search range until left == right.

# When left and right meet, the minimum element is at that position.

# Return the element at index left.


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