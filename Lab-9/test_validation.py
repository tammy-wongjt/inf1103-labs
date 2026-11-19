from supplier import Supplier
from product_factory import ProductFactory
from orderline import OrderLine

supplier = Supplier("S001", "Tech Ltd", "a@b.com")

# Test 1: Negative price should crash
try:
    ProductFactory.create("physical", "P001", "Laptop", -100, 10, supplier, 2.5)
except ValueError as e:
    print(f"Caught: {e}") # Caught: Price must be greater than zero.

# Test 2: Negative stock should crash
try:
    ProductFactory.create("digital", "P002", "E-book", 10, -5, supplier, 5.2)
except ValueError as e:
    print(f"Caught: {e}") # Caught: Stock quantity cannot be negative.

# Test 3: Zero quantity in OrderLine should crash
try:
    product = ProductFactory.create("physical", "P003", "Mouse", 50, 10, supplier, 0.1)
    OrderLine(product, 0)
except ValueError as e:
    print(f"Caught: {e}") # Caught: Quantity must be greater than zero.

# Test 4: Valid inputs work fine
try:
    p = ProductFactory.create("physical", "P004", "Keyboard", 100, 5, supplier, 1.0)
    line = OrderLine(p, 2)
    print("Valid product and order line created successfully!")
except ValueError as e:
    print(f"Unexpected error: {e}")