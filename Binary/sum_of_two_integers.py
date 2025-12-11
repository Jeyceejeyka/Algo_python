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



# Step-by-Step Explanation of the while loop
#  Condition:
# while i >= 0 or j >= 0 or carry:


# This says: keep looping as long as any of these are true:

# There are still digits left in a (i >= 0)

# There are still digits left in b (j >= 0)

# There is a carry to add (carry != 0)

# This is why the loop stops only when all digits are processed and there’s no carry.

#  Start each loop with the carry
# total = carry


# Initialize total with the carry from the previous addition.

# Add the digit from a (if any)
# if i >= 0:
#     total += int(a[i])
#     i -= 1


# If i is valid (there are still digits in a):

# Convert the character to an integer

# Add it to total

# Move the pointer left (i -= 1)

#  Add the digit from b (if any)
# if j >= 0:
#     total += int(b[j])
#     j -= 1


# Same as above for b.

#  Calculate the current bit
# result = str(total % 2) + result


# % 2 gives the remainder, which is the current binary digit (0 or 1).

# Prepend it to result because we are building the string from right to left.

#  Update carry
# carry = total // 2


# // 2 gives the carry for the next column.

# Example:

# total = 3 → carry = 1, current bit = 1

# total = 2 → carry = 1, current bit = 0

# total = 1 → carry = 0, current bit = 1

# Loop repeats

# After updating i, j, and carry, the while loop checks the condition again.

# Stops only when all digits are processed AND carry = 0.

# Return final result
# return result


# At this point, result contains the full binary sum as a string.

# Example Trace: "11" + "1"
# Step	i	j	carry	total	digit added	result
# 1	1	0	0	1+1+0=2	0	"0"
# 2	0	-1	1	1+0+1=2	0	"00"
# 3	-1	-1	1	0+0+1=1	1	"100"

# Final result: "100"



# Complexity Analysis
# -----------------------

# Let:

# n = len(a)

# m = len(b)

# 1. Time Complexity

# Loop runs max(n, m) + 1 times → O(n + m)

# append is O(1) each

# reversed + join is O(n + m)

#  Total time complexity = O(n + m)

# 2. Space Complexity

# We store the result in a list of length ≤ max(n, m) + 1

# O(n + m) space

#  Why this is the best

# You cannot do better than O(n + m) because you must look at each digit at least once.

# Using a list avoids repeated string concatenation (which would make it O((n + m)²)).



# Example:

# Input:  a = "11", b = "1"
# Output: "100"


# Constraints:

# 1 ≤ a.length, b.length ≤ 10⁴

# Each string contains only '0' or '1'.

# Strings do not contain leading zeros except the value "0".

# 2. Sum of Two Integers — (Commonly known as “Add Without + or -”)

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