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

def load_inventory():
    """
    Load inventory from inventory.json.
    If the file doesn't exist, return the default 3 products.
    """
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("inventory.json not found. Starting with default inventory.")
        return [
            {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
            {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
            {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
        ]
    
def main():
    # #Phase 1: hardcode the product
    # inventory = [
    #     {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    #     {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    #     {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
    # ]
    inventory  = load_inventory()

    display_all(inventory)

if __name__ == "__main__":
    main()