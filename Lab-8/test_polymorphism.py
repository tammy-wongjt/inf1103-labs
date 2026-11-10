from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

print("--- Testing Polymorphism ---")

supplier = Supplier("S001", "Tammy", "twjt@gmail.com")
p1 = PhysicalProduct("P001", "Phone", 2000, 300, supplier, 0.5)
p2 = DigitalProduct("P002", "E-Book", 15.99, 999, supplier, 5.2)

inv = Inventory()
inv.add_product(p1)
inv.add_product(p2)

for product in inv.get_products():
    product.display_information()
    print(f"Fulfilment: {product.get_fulfilment_info()}")
    print("-" * 40)