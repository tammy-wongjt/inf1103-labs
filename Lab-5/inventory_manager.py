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

def main():
    #Phase 1: hardcode the product
    inventory = [
        {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
        {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
        {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
    ]

    display_all(inventory)

if __name__ == "__main__":
    main()