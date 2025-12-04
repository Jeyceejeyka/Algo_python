# # Function to calculate purchase cost based on item selections
# def calculate_total(item1=False, item2=False, item3=False):
#     # Prices of individual items
#     price1 = 15
#     price2 = 25
#     price3 = 30

#     # Determine which items were selected
#     items_chosen = []
#     if item1: items_chosen.append(price1)
#     if item2: items_chosen.append(price2)
#     if item3: items_chosen.append(price3)

#     # Base cost without discount
#     base_total = sum(items_chosen)

#     # Decide which discount applies
#     if len(items_chosen) == 1:
#         discount_rate = 0        
#     elif len(items_chosen) == 2:
#         discount_rate = 0.10     
#     else:
#         discount_rate = 0.25     
#     # Calculate final cost
#     discount_amount = base_total * discount_rate
#     final_total = base_total - discount_amount

#     print("---- Output of Online Store ----")
#     print(f"Items selected: {len(items_chosen)}")
#     print(f"Base cost: ${base_total}")
#     print(f"Discount applied: {discount_rate * 100}%")
#     print(f"Final total: ${final_total}\n")

#     return final_total


# calculate_total(item1=True)
# calculate_total(item1=True, item2=True)
# calculate_total(item1=True, item2=True, item3=True)


# # Find unique combinations?
# from itertools import combinations
# from typing import List, Any

# def unique_combinations(items: List[Any], r: int) -> List[tuple]:
#     """
#     Returns all unique combinations of length r from the given list.
    
#     :param items: List of elements
#     :param r: Length of each combination
#     :return: List of unique combinations (as tuples)
#     """
#     return list(combinations(items, r))

# # Example usage
# my_list = [1, 2, 3, 4]
# result = unique_combinations(my_list, 2)
# print(result)



# # 🔹 Explanation:

# # itertools.combinations(items, r) generates all r-length combinations without repetition.

# # The result is always unique tuples.

# # You can change r to get different combination lengths.

# # The order of elements in each tuple doesn’t matter (so (1,2) is the same as (2,1)).






day_of_week = "Wednesday"

if day_of_week in ["Saturday", "Sunday"]:
    schedule = "Relax, no work"
elif day_of_week in ["Monday", 
                    "Tuesday",
                    "Wednesday", 
                    "Thursday", 
                    "Friday"]:
    schedule = "Workday"
else:
    schedule = "Invalid day"

print(schedule)  

score = 67

if score >= 50:  # Outer condition checks if student passed
    if score % 2 == 0:  # Inner condition checks if score is even
        print("Passed with an even score")
    else:  # Executes if score is odd
        print("Passed with an odd score")
else:  # Executes if score is below 50
    print("Failed")
# Output: Passed with an odd score
# Explanation: score >= 50 is True, but score % 2 == 0 is False, so the else block executes.

score = 67

if score >= 50 and score % 2 == 0:  # Combined condition for passing and even score
    print("Passed with an even score")
elif score >= 50:  # Checks if score is passing but odd
    print("Passed with an odd score")
else:  # Score is below 50
    print("Failed")
# Output: Passed with an odd score
# Explanation: Same logic as before, but code is cleaner and easier to follow.
