# Counting Bits
# Problem Statement

# Given an integer n, return an array ans of length n + 1 such that for each i (0 ≤ i ≤ n), ans[i] is the number of 1’s in the binary representation of i.
# solution: A simple approach is to iterate through each number from 0 to n, convert each number to its binary representation using the built-in bin() function, and count the number of 1's using the count() method. We store these counts in a list and return it.
# complexity: Time Complexity: O(n log n), where n is the input integer. For each number from 0 to n, converting it to binary and counting the 1's takes O(log n) time.
# Space Complexity: O(n), as we store the result in a list of size n + 1.
# def counting_bits(n: int):
#     ans = []
#     for i in range(n + 1):
#         # Count the number of 1's in the binary representation of i
#         count_ones = bin(i).count('1')
#         ans.append(count_ones)
#     return ans
    


#SOLUTION: Bit Manipulation
# Another efficient approach is to use bit manipulation. The number of 1's in the binary representation of a number can be derived from the number of 1's in the binary representation of the 
# number obtained by removing the least significant bit (i.e., i >> 1) plus 1 if the least significant bit is 1 (i.e., i & 1).
# complexity: Time Complexity: O(n), where n is the input integer. We iterate through each number from 1 to n once.
# Space Complexity: O(n), as we store the result in a list of size n + 1.
def counting_bits(n: int):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans


# Solution: C Simple Approach
# A simpler approach is to use the relationship between the number of 1's in the binary representation of a number and its half. The number of 1's in i is equal to the number of 1's in i // 2 plus 1 if i is odd.
# complexity: Time Complexity: O(n), where n is the input integer. We iterate through each number from 1 to n once.
# Space Complexity: O(n), as we store the result in a list of size n + 1.
def countBits_simple(n: int):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        half = i // 2         # number without last bit
        last_bit = i % 2      # last bit (0 or 1)
        ans[i] = ans[half] + last_bit
    return ans

# Example
print(countBits_simple(5))  # Output: [0, 1, 1, 2, 1, 2]


# Example 1

# Input:

# n = 2


# Output:

# [0, 1, 1]


# Explanation:

# 0 → 0 → 0 ones

# 1 → 1 → 1 one

# 2 → 10 → 1 one

# Example 2

# Input:

# n = 5



# Output:

# [0, 1, 1, 2, 1, 2]


# Explanation:

# 0 → 0 → 0

# 1 → 1 → 1

# 2 → 10 → 1

# 3 → 11 → 2

# 4 → 100 → 1

# 5 → 101 → 2

# Constraints

# 0 ≤ n ≤ 10⁵