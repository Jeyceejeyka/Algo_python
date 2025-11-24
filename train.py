# Function to calculate purchase cost based on item selections
def calculate_total(item1=False, item2=False, item3=False):
    # Prices of individual items
    price1 = 15
    price2 = 25
    price3 = 30

    # Determine which items were selected
    items_chosen = []
    if item1: items_chosen.append(price1)
    if item2: items_chosen.append(price2)
    if item3: items_chosen.append(price3)

    # Base cost without discount
    base_total = sum(items_chosen)

    # Decide which discount applies
    if len(items_chosen) == 1:
        discount_rate = 0        
    elif len(items_chosen) == 2:
        discount_rate = 0.10     
    else:
        discount_rate = 0.25     
    # Calculate final cost
    discount_amount = base_total * discount_rate
    final_total = base_total - discount_amount

    print("---- Output of Online Store ----")
    print(f"Items selected: {len(items_chosen)}")
    print(f"Base cost: ${base_total}")
    print(f"Discount applied: {discount_rate * 100}%")
    print(f"Final total: ${final_total}\n")

    return final_total


calculate_total(item1=True)
calculate_total(item1=True, item2=True)
calculate_total(item1=True, item2=True, item3=True)
