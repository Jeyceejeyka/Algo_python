# Counting Bits
# Problem Statement

# Given an integer n, return an array ans of length n + 1 such that for each i (0 ≤ i ≤ n), ans[i] is the number of 1’s in the binary representation of i.
# solution: A simple approach is to iterate through each number from 0 to n, convert each number to its binary representation using the built-in bin() function, and count the number of 1's using the count() method. We store these counts in a list and return it.
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
def counting_bits(n: int):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans


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