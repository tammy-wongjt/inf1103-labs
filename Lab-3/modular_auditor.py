def main():
    inventory = 0
    failed_entries = 0
    deliveries_processed = 0
    total_tax = 0.0

    while True:
        result = get_valid_input()

        #if user quit
        if result is None:
            break

        #invalid input
        if result == -1:
            failed_entries += 1
            continue

        #valid delivery
        inventory = process_delivery(inventory, result)
        tax = calculate_tax(result)
        total_tax += tax
        deliveries_processed += 1

        print(f"Current inventory: {inventory}")
        print(f"Tax for this delivery: ${tax:.2f}")

        #overstock alert
        if inventory > 500:
            print("Overstock alert! Inventory exceeded 500 units.")
            break

    generate_report(inventory, failed_entries, deliveries_processed, total_tax)


def get_valid_input():
    user_input = input("Enter stock quantity (or 'quit' to exit): ")

    # user quits
    if user_input.lower() == 'quit':
        return None

    # if input is not a number (invalid)
    if not user_input.isdigit():
        print("Error. Please enter a valid positive number")
        return -1   # invalid

    return int(user_input)

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.1  #10% tax

def generate_report(total_units, failed_attempts, deliveries_processed, total_tax):
    print(f"Total units processed: {total_units}")
    print(f"Total Deliveries Processed: {deliveries_processed}")
    print(f"Number of failed/rejected entries: ", failed_attempts)
    print(f"Total tax collected: ${total_tax:.2f}")


if __name__ == "__main__":
    main()


# # 1. Initialize the inventory to zero in the start
# inventory = 0
# failed_entries = 0  # need for requirement no. 8

# # 2. Run in a continuous loop asking user to enter a stock quantity, until the user types quit.
# while True:
#     user_input = input("Enter stock quantity (or 'quit' to exit): ")

#     if user_input.lower() == 'quit':
#         break

#     # 3. Accept stock values as integers.
#     # 4. Handle invalid input: If the user enters a string (e.g., "ten"), reject it, print an error, and move to the next iteration.
#     if not user_input.isdigit():
#         print("Error: Please enter a number.")
#         failed_entries += 1
#         continue

#     quantity = int(user_input)

#     # Enforce business rules: Reject negative numbers
#     if quantity < 0:
#         print("Error: Negative numbers are not allowed.")
#         failed_entries += 1
#         continue

#     # 6. Manage State: Keep a running total of the inventory.
#     inventory += quantity
#     print(f"Current inventory: {inventory}")

#     # 7. Trigger Overstock Alert: If the total inventory exceeds 500 units
#     if inventory > 500:
#         print("Overstock Alert! Inventory Exceeded 500 units.")
#         break

# # 8. Reporting: When the user types quit, print the Total Units Processed and the Number of Failed/Rejected Entries.
# print("\n--- Audit Report ---")
# print(f"Total Units Processed: {inventory}")
# print(f"Number of Failed/Rejected Entries: {failed_entries}")