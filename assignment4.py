# Stage 3: Full formula A = P * (1 + r) ** t
def compound_interest(principal, rate, years):
    return principal * (1 + rate) ** years

# Test 1
print(compound_interest(1000, 0.05, 5))  
# Test 2
print(compound_interest(1500, 0.03, 10))  

# Test 3
print(compound_interest(2000, 0.07, 3))  
