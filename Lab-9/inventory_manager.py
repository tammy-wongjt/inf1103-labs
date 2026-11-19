import json
from product import Product
from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier
from product_factory import ProductFactory
import csv
from order import Order
from orderline import OrderLine
from discounts import NoDiscount, PercentageDiscount, BulkDiscount, StudentDiscount


FILENAME = "inventory.json"


# ---------- File Handling ----------
def load_inventory() -> Inventory:
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


def save_inventory(inventory: Inventory) -> None:
    """Save the inventory to JSON."""
    print("Saving inventory...")
    with open(FILENAME, "w") as f:
        json.dump(inventory.to_list_of_dicts(), f, indent=4)
    print(f"Inventory saved successfully to {FILENAME}.")


def get_positive_float(prompt: str) -> float:
    """Keep asking until the user enters a valid number greater than zero."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")


def get_non_negative_int(prompt: str) -> int:
    """Keep asking until the user enters a valid whole number that is 0 or greater."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a number that is zero or greater.")
                continue
            return value
        except ValueError:
            print("Please enter a valid whole number.")


def get_positive_int(prompt: str) -> int:
    """Keep asking until the user enters a valid whole number greater than zero."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid whole number.")

# ---------- Menu Actions ----------

def handle_add(inventory: Inventory) -> None:
    print("Add New Product")
    product_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()

    price = get_positive_float("Price: ")
    stock = get_non_negative_int("Stock Quantity: ")

    # Create supplier
    print("\nSupplier Information")
    supplier_id = input("Supplier ID: ").strip()
    supplier_name = input("Supplier Name: ").strip()
    supplier_email = input("Supplier Contact Email: ").strip()
    supplier = Supplier(supplier_id, supplier_name, supplier_email)

    print("Product type:")
    print("  1. Physical")
    print("  2. Digital")
    type_choice = input("Choose (1/2): ").strip()

    new_product: Product

    if type_choice == "1":
        weight = get_positive_float("Weight (kg): ")
        new_product = ProductFactory.create("physical", product_id, name, price, stock, supplier, weight)
    elif type_choice == "2":
        download_size = get_positive_float("Download Size (MB): ")
        new_product = ProductFactory.create("digital", product_id, name, price, stock, supplier, download_size)
    else:
        print("Invalid type.")
        return

    if inventory.add_product(new_product):
        print("Product added successfully!")



def handle_update(inventory: Inventory) -> None:
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip()

    product = inventory.find_product(product_id)
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


def handle_search(inventory: Inventory) -> None:
    print("Search Product")
    product_id = input("Enter Product ID: ").strip()

    product = inventory.find_product(product_id)
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

def handle_remove(inventory: Inventory) -> None:
    print("Remove Product")
    product_id = input("Enter Product ID: ").strip()
    inventory.remove_product(product_id)


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    """Load products from a CSV file and add them to the inventory."""
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        loaded = 0
        with file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header row
            for row in reader:
                try:
                    # row: [product_type, product_id, name, price, stock_quantity]
                    product_type = row[0]
                    product_id = row[1]
                    name = row[2]
                    price = float(row[3])   # This will raise ValueError for "abc"
                    stock = int(row[4])
                    
                    product = ProductFactory.create(
                        product_type, product_id, name, price, stock, supplier, 0.0
                    )
                    if inventory.add_product(product):
                        loaded += 1
                except ValueError as e:
                    print(f"Skipping invalid row {row}: {e}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")

def handle_order(inventory: Inventory) -> None:
    print("Create a New Order")
    order_id = input("Order ID: ").strip()
    order = Order(order_id)

    while True:
        product_id = input("Enter Product ID to add (or 'done' to finish): ").strip()
        if product_id.lower() == 'done':
            break
        product = inventory.find_product(product_id)
        if product is None:
            print("Product not found.")
            continue
        
        try:
            quantity = int(input("Quantity: "))
            line = OrderLine(product, quantity) # This will test your validation!
            order.add_order_line(product, quantity)
            print("Item added to order.")
        except ValueError as e:
            print(f"Error: {e}") # Catches negative/zero quantity

    # Apply Discount
    print("\nApply Discount:")
    print("1. No Discount")
    print("2. Percentage (10%)")
    print("3. Bulk ($20 off if total >= 200)")
    print("4. Student (5% off)")
    choice = input("Choose (1-4): ").strip()

    if choice == "2":
        order.set_discount(PercentageDiscount(10))
    elif choice == "3":
        order.set_discount(BulkDiscount(200, 20))
    elif choice == "4":
        order.set_discount(StudentDiscount())
    else:
        order.set_discount(NoDiscount())

    # Display the result
    print("\n--- Order Summary ---")
    order.display_information() # If you have this method
    print(f"Final Total: ${order.calculate_total():.2f}")


def print_menu() -> None:
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Remove Product")
    print("6. Create Order & Apply Discount")
    print("7. Save Inventory")
    print("8. Exit")
    print("----------------------------")


# ---------- Main ----------
def main() -> None:
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
            handle_remove(inventory)
        elif option == "6":
            handle_order(inventory)
        elif option == "7":
            save_inventory(inventory)
        elif option == "8":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()