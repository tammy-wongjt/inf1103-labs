from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory

# Setup
supplier = Supplier("S001", "Tammy", "twjt@gmail.com")

# Create a product before it goes into any inventory
product = PhysicalProduct("P001", "Phone", 2000, 300, supplier, 0.5)
print("--- Aggregation Test ---")
print("Product created independently:")
product.display_information()

# Put it into Inventory A
inv_a = Inventory()
inv_a.add_product(product)
print(f"\nAdded to Inventory A. Count: {inv_a.count()}")

# Remove it from Inventory A
inv_a.remove_product("P001")
print(f"Removed from Inventory A. Is empty: {inv_a.is_empty()}")

# Prove the product still exists and works after being removed
print("\nChecking if the product survived removal:")
product.display_information()

# Move the same product to Inventory B
inv_b = Inventory()
inv_b.add_product(product)
print(f"\nMoved to Inventory B. Count: {inv_b.count()}")

# Verify it's the exact same object reference
print(f"Same object reference in Inventory B? {product is inv_b.find_product('P001')}")

# Clear Inventory B
inv_b.remove_product("P001")

# The product should still exist even though both inventories are empty
print("\nBoth inventories are empty, but the product still exists:")
product.display_information()