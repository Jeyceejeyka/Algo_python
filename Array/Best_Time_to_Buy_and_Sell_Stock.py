# 📘 Best Time to Buy and Sell Stock (LeetCode 121)
# 🟦 Problem Statement

# You are given an array prices where prices[i] is the price of a given stock on the i-th day.

# You want to maximize your profit by choosing a single day to buy one stock and a different day in the future to sell it.

# Return the maximum profit you can achieve.
# If you cannot achieve any profit, return 0.

# 📌 Example 1

# Input:
# prices = [7,1,5,3,6,4]

# Output:
# 5

# Explanation:
# Buy on day 1 (price = 1),
# Sell on day 4 (price = 6),
# Profit = 6 - 1 = 5.


# solution1: # with time complexity O(n)
def max_profit(prices):
    min_price = float('inf')
    # float('inf') is a Python way of creating positive infinity. It represents a value that is larger than any other numerical value.
    max_price = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_price:
            max_price = price - min_price
    return max_price


print(max_profit([7,61,5,3,6,4]))  # Output: 5
print(max_profit([7,6,4,33,1]))    # Output: 0

# 📌 Example 2

# Input:
# prices = [7,6,4,3,1]

# Output:
# 0

# Explanation:
# No profitable transaction exists.

# 🧷 Constraints

# 1 <= prices.length <= 10^5

# 0 <= prices[i] <= 10^4