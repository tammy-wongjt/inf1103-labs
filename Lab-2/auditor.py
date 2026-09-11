# 1. Initialize the inventory to zero in the start
inventory = 0
failed_entries = 0  # need for requirement no. 8

# 2. Run in a continuous loop asking user to enter a stock quantity, until the user types quit.
while True:
    user_input = input("Enter stock quantity (or 'quit' to exit): ")

    if user_input.lower() == 'quit':
        break

    # 3. Accept stock values as integers.
    # 4. Handle invalid input: If the user enters a string (e.g., "ten"), reject it, print an error, and move to the next iteration.
    if not user_input.isdigit():
        print("Error: Please enter a number.")
        failed_entries += 1
        continue

    quantity = int(user_input)

    # Enforce business rules: Reject negative numbers
    if quantity < 0:
        print("Error: Negative numbers are not allowed.")
        failed_entries += 1
        continue

    # 6. Manage State: Keep a running total of the inventory.
    inventory += quantity
    print(f"Current inventory: {inventory}")

