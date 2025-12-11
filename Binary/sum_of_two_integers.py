# 1. Binary — (Commonly known as “Add Binary”)

# Problem Statement:
# You are given two binary strings a and b.
# Return the sum of the two numbers as a binary string.

def addBinary(a: str, b: str) -> str:
    a_left, b_left = len(a)-1, len(b) -1
    carry = 0
    result = []
    
    
    while a_left >= 0 or b_left >= 0 or carry:
        total = carry
        
        
        if a_left >= 0:
            total += int(a[a_left])
            a_left -= 1
            
            
        if b_left >= 0:
            total += int(b[b_left])
            b_left -= 1
        carry = total // 2
        result.append(str(total % 2))   
        
    return ''.join(reversed(result))

print(addBinary("11", "1"))
print(addBinary("1010", "1011"))

# Example:

# Input:  a = "11", b = "1"
# Output: "100"


# Constraints:

# 1 ≤ a.length, b.length ≤ 10⁴

# Each string contains only '0' or '1'.

# Strings do not contain leading zeros except the value "0".

# ✅ 2. Sum of Two Integers — (Commonly known as “Add Without + or -”)

# Problem Statement:
# Given two integers a and b, return their sum,
# but you are not allowed to use the operators + or -.

# You must compute the result using bitwise operations.

# Example:

# Input:  a = 1, b = 2
# Output: 3


# Constraints:

# -1000 ≤ a, b ≤ 1000 (may vary slightly depending on the platform)

# The result fits in a signed 32-bit integer.