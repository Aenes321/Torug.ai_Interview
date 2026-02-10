# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_average_order_value(orders):
    total = 0
    count = 0
    
    for order in orders:
        try: #to avoid dictionary key error
            if order["status"] != "cancelled":
                total += order["amount"]
                count += 1
        except (KeyError,TypeError):
            print("missing or wrong key")
    if(count != 0): # to avoid 0 zero divison error
        return total / count
    else:
        return 0
    