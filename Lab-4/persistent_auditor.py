FILENAME = "inventory.txt"

def load_inventory():
    try: 
        with open(FILENAME, "r") as f:
            lines = f.read().strip().split("\n")
    except FileNotFoundError:
        return 0, []

    total = 0
    history = []
    for line in lines:
        line = line.strip()
        if line.startswith("Total:"):
            total = int(line.replace("Total:", "").strip())
        elif line.isdigit():
            history.append(int(line))

    return total, history

def save_inventory(total, history):
    with open(FILENAME, "w") as f:
        f.write(f"Total: {total}\n")
        f.write("History:\n")
        for amount in history:
            f.write(f"{amount}\n")
    print(f"\nInventory saved to {FILENAME}")

def main():
    inventory, history = load_inventory()

    failed_entries = 0
    deliveries_processed = 0
    total_tax = 0.0

    print(f"Starting inventory: {inventory}")
    print(f"Previous transactions: {len(history)}")

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

        history.append(result)

        print(f"Current inventory: {inventory}")
        print(f"Tax for this delivery: ${tax:.2f}")

        #overstock alert
        if inventory > 500:
            print("Overstock alert! Inventory exceeded 500 units.")
            break

    save_inventory(inventory, history)

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

