from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order

# Setup
supplier = Supplier("S001", "Tammy", "twjt@gmail.com")
p1 = PhysicalProduct("P001", "Phone", 2000, 300, supplier, 0.5)
p2 = DigitalProduct("P002", "E-Book", 15.99, 999, supplier, 5.2)

print("--- Composition Test ---")

# Create Order A and add products
print("Creating Order A:")
order_a = Order("ORD-A-001")
order_a.add_order_line(p1, 2)    # 2 laptops
order_a.add_order_line(p2, 5)    # 5 e-books
order_a.display_information()

# Create Order B with the same products
print("\nCreating Order B with the same products:")
order_b = Order("ORD-B-002")
order_b.add_order_line(p1, 1)    # 1 laptop
order_b.display_information()

# Check the counts
lines_a = order_a.get_order_lines()
lines_b = order_b.get_order_lines()

print(f"\nOrderLines in Order A: {len(lines_a)}")
print(f"OrderLines in Order B: {len(lines_b)}")
print(f"Total OrderLines created: {len(lines_a) + len(lines_b)} (each order creates its own)")

# Prove the Product is shared, but OrderLines are unique to each Order
print(f"\nOrder A references the shared p1: {lines_a[0].get_product() is p1}")
print(f"Order B references the shared p1: {lines_b[0].get_product() is p1}")
print(f"Are the two OrderLines the exact same object? {lines_a[0] is lines_b[0]}")

# Remove a line from Order A and verify Order B is unaffected
print("\nRemoving a line from Order A:")
order_a.remove_order_line(0)
print(f"Order A now has {len(order_a.get_order_lines())} line(s)")
print(f"Order B still has {len(order_b.get_order_lines())} line(s)")

# Prove the Product itself wasn't destroyed by the OrderLine removal
print("\nChecking if the Product survived the OrderLine removal:")
p1.display_information()