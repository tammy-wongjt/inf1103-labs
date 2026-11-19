from supplier import Supplier
from product_factory import ProductFactory

supplier = Supplier("S001", "Tech Ltd", "a@b.com")

# Test 1: Create a physical product
p1 = ProductFactory.create("physical", "P001", "Laptop", 1200.00, 10, supplier, 2.5)
print(f"Created: {p1.get_name()} | Weight: {p1.get_weight()} kg")

# Test 2: Create a digital product
p2 = ProductFactory.create("digital", "P002", "E-Book", 15.99, 999, supplier, 5.2)
print(f"Created: {p2.get_name()} | Download size: {p2.get_download_size()} MB")

# Test 3: Unknown type (should raise ValueError)
try:
    p3 = ProductFactory.create("service", "P003", "Consulting", 500.00, 1, supplier)
except ValueError as e:
    print(f"Caught error: {e}")