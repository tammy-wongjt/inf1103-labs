import json

FILENAME = "inventory.json"

def display_all(inventory):
    #print all products in inventory
    if not inventory:
        print("Inventory is empty.")
        return

    print("Current Inventory")
    print("-" * 20)
    for product in inventory:
        print(f"ID: {product['id']} |  Name: {product['name']} | Price: {product['price']:.2f} | Stock: {product['stock']}")
    print("-" * 20)

def add_product(inventory):
    # prompt for new product and add to inventory
    print("Add new product")
    product_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()

    try: 
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Error: Price must be a number, stock must be an integer.")
        return

    # check for duplicate ID
    for product in inventory:
        if product["id"] == product_id:
            print(f"Error. Product ID {product_id} already exists.")
            return

    new_product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }
    inventory.append(new_product)
    print("Product added successfully!")

def search_product(inventory):
    """Search for a product by ID."""
    print("Search Product")
    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found")
            print("-" * 48)
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("-" * 48)
            return

    print("Product not found.")

def print_menu():
    """Print the main menu."""
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

def update_stock(inventory):
    """Update stock for an existing product."""
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")

            try:
                new_stock = int(input("New Stock Quantity: "))
            except ValueError:
                print("Error: Stock must be an integer.")
                return

            product["stock"] = new_stock
            print("Stock updated successfully!")
            return

    print("Product not found.")

def load_inventory():
    """
    Load inventory from inventory.json.
    If the file doesn't exist, return the default 3 products.
    """
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
            print("inventory.json found.")
            print("Inventory loaded successfully.")
            return data
    except FileNotFoundError:
        print("inventory.json not found. Starting with default inventory.")
        return []
    except json.JSONDecodeError:
        print("inventory.json is corrupted. Starting with empty inventory")
        return []

def save_inventory(inventory):
    # write to json file
    print("Saving inventory...")
    with open(FILENAME, "w") as f:
        json.dump(inventory, f, indent=4)
    print(f"Inventory saved successfully to {FILENAME}.")
    
def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory()

    while True:
        print_menu()
        option = input("Enter option: ").strip()

        if option == "1":
            display_all(inventory)
        elif option == "2":
            add_product(inventory)
        elif option == "3":
            update_stock(inventory)
        elif option == "4":
            search_product(inventory)
        elif option == "5":
            save_inventory(inventory)
        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()