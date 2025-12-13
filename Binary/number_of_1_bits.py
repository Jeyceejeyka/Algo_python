# Number of 1 Bits (LeetCode #191)

# Problem Statement:
# Write a function that takes an unsigned integer and returns the number of '1' bits it has.
# This count is also known as the Hamming weight.

# Example 1
# Input:  n = 00000000000000000000000000001011
# Output: 3
# solution: A simple approach is to iterate through each character in the binary string and count the number of '1's.
def number_of_1_bits(n: str): 
    count = 0
    for char in n:
        if char == '1':
            count += 1
            
    return count


# solution using built-in function 
def numer_of_1_bits_simple_func(n: str) -> int:
    return n.count('1')


# Test Cases:
print(number_of_1_bits('00000000000000000000000000001011'))  
print(number_of_1_bits('00000000000000000000000010000000'))  
print(number_of_1_bits('11111111111111111111111111101'))  
print(numer_of_1_bits_simple_func('00000000000000000000000000001011')) 
print(numer_of_1_bits_simple_func('00000000000000000000000010000000'))  
print(numer_of_1_bits_simple_func('11111111111111111111111111101'))  
    
# Explanation:
# The input binary string has three '1' bits.

# Example 2
# Input:  n = 00000000000000000000000010000000
# Output: 1

# Example 3
# Input:  n = 11111111111111111111111111111101
# Output: 31

# Constraints

# The input must be treated as an unsigned integer.

# The input value fits in a 32-bit integer.