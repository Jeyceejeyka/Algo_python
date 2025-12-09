# Problem: Container With Most Water

# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the line i are located at (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container holds the most water.

# Return the maximum amount of water a container can store.

# Notice: You may not slant the container.

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
