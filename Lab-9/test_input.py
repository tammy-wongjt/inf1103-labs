from inventory_manager import get_positive_float

print("Enter a price (try abc, then -5, then 12.50):")
price = get_positive_float("Price: ")
print(f"Returned value: {price} (type: {type(price).__name__})")