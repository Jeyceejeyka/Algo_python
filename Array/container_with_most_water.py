# Problem: Container With Most Water

# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the line i are located at (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container holds the most water.

# Return the maximum amount of water a container can store.

# Notice: You may not slant the container.

def container_with_most_water(arr):
    left = 0
    right = len(arr) - 1
    max_area = 0
    
    
    while left < right:
        width = right -left
        height = min(arr[left], arr[right])
        current_area = width * height
        max_area = max(max_area, current_area)
        # Move the pointer pointing to the shorter line
        if arr[left] < arr[right]:
            left += 1   
        else:
            right -= 1
    return max_area

print(container_with_most_water([1,8,6,2,5,4,8,3,7]))  # Output: 49
print(container_with_most_water([1,1]))  # Output: 1    

# Here’s the step-by-step approach to solve “Container With Most Water” in a commented list format you can follow or translate into code:

# Step-by-step solution (commented list)

# Start with two pointers

# left at the start of the array (index 0)

# right at the end of the array (last index)

# max_area = 0 to keep track of the largest area

# Loop until pointers meet

# While left < right, do the following:

# Calculate width

# width = right - left

# This is the distance between the two lines

# Determine the container height

# height = min(arr[left], arr[right])

# Water level is limited by the shorter line

# Calculate current area

# current_area = width * height

# Update maximum area

# max_area = max(max_area, current_area)

# Move the pointer pointing to the shorter line

# If arr[left] < arr[right]: move left += 1

# Else: move right -= 1

# Reason: moving the shorter line may give a taller line in the next step → chance for bigger area

# Moving the taller line won’t help because height is still limited by the shorter line

# Repeat steps 3–7

# Continue shrinking the window until left >= right

# Return the largest area

# After loop ends, max_area contains the maximum water area

# Optional tip for implementation

# Keep everything in O(n) time and O(1) space

# Don’t try to check all pairs (O(n²))

# This is the “two-pointer greedy” optimal approach



# Example 1

# Input:

# height = [1,8,6,2,5,4,8,3,7]


# Output:

# 49


# Explanation:
# The lines at index 1 (height=8) and index 8 (height=7) form the largest container
# → min(8,7) * distance(8-1 = 7) = 7 * 7 = 49

# Example 2

# Input:

# height = [1,1]


# Output:

# 1

# Constraints
# n == height.length
# 2 ≤ n ≤ 10^5
# 0 ≤ height[i] ≤ 10^4

# problem meaning

# Pick two bars → calculate area → maximize area

# area = min(height[left], height[right]) * (right - left)
