import json
from product import Product
from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

FILENAME = "inventory.json"


# ---------- File Handling ----------
def load_inventory():
    """Load inventory.json and return an Inventory object."""
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
            print("inventory.json found.")
            print("Inventory loaded successfully.")
            inventory = Inventory()
            inventory.load_from_list_of_dicts(data)
            return inventory
    except FileNotFoundError:
        print("inventory.json not found. Starting with empty inventory.")
        return Inventory()
    except json.JSONDecodeError:
        print("inventory.json is corrupted. Starting with empty inventory.")
        return Inventory()


def save_inventory(inventory):
    """Save the inventory to JSON."""
    print("Saving inventory...")
    with open(FILENAME, "w") as f:
        json.dump(inventory.to_list_of_dicts(), f, indent=4)
    print(f"Inventory saved successfully to {FILENAME}.")


# ---------- Menu Actions ----------

def handle_add(inventory):
    print("Add New Product")
    product_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Error: Price must be a number, stock must be an integer.")
        return

    print("Product type:")
    print("  1. Physical")
    print("  2. Digital")
    type_choice = input("Choose (1/2): ").strip()

    if type_choice == "1":
        try:
            weight = float(input("Weight (kg): "))
        except ValueError:
            print("Error: Weight must be a number.")
            return
        new_product = PhysicalProduct(product_id, name, price, stock, weight)
    elif type_choice == "2":
        try:
            download_size = float(input("Download size (MB): "))
        except ValueError:
            print("Error: Download size must be a number.")
            return
        new_product = DigitalProduct(product_id, name, price, stock, download_size)
    else:
        print("Invalid type.")
        return

    if inventory.add_product(new_product):
        print("Product added successfully!")


def handle_update(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip()

    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")

    try:
        new_stock = int(input("New Stock Quantity: "))
    except ValueError:
        print("Error: Stock must be an integer.")
        return

    if inventory.update_stock(product_id, new_stock):
        print("Stock updated successfully!")


def handle_search(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ").strip()

    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print("-" * 48)
    product.display_information()
    print(f"Fulfilment: {product.get_fulfilment_info()}")
    if hasattr(product, "calculate_shipping_cost"):
        print(f"Shipping cost: ${product.calculate_shipping_cost():.2f}")
    print("-" * 48)


def print_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


# ---------- Main ----------
def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory()

    while True:
        print_menu()
        option = input("Enter option: ").strip()

        if option == "1":
            inventory.display_all()
        elif option == "2":
            handle_add(inventory)
        elif option == "3":
            handle_update(inventory)
        elif option == "4":
            handle_search(inventory)
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