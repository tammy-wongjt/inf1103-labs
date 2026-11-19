from inventory import Inventory
from supplier import Supplier
from inventory_manager import load_products

# Create a dummy supplier
supplier = Supplier("S001", "Tech Ltd", "a@b.com")
inventory = Inventory()

print("--- Testing with missing file ---")
load_products("nonexistent.csv", inventory, supplier)

print("\n--- Testing with products.csv ---")
load_products("products.csv", inventory, supplier)

print("\n--- Displaying loaded inventory ---")
inventory.display_all()