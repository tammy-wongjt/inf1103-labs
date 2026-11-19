from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from discounts import NoDiscount, PercentageDiscount, BulkDiscount, StudentDiscount

# Setup
supplier = Supplier("S001", "Tech Ltd", "a@b.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.00, 10, supplier, 2.5)
mouse = PhysicalProduct("P002", "Mouse", 50.00, 50, supplier, 0.1)

# Create a new order for the $250 test
print("\n--- Section 2.3 Prediction Test ($250 total) ---")
order_predict = Order("ORD-PREDICT")
# Mouse is $50. Add 5 of them to get exactly $250
order_predict.add_order_line(mouse, 5) 

print(f"Subtotal: ${sum(line.calculate_subtotal() for line in order_predict.get_order_lines()):.2f}")

# 1. Test BulkDiscount(200, 20)
order_predict.set_discount(BulkDiscount(200, 20))
print(f"With BulkDiscount(200, 20): ${order_predict.calculate_total():.2f}") 

# 2. Test PercentageDiscount(10)
order_predict.set_discount(PercentageDiscount(10))
print(f"With PercentageDiscount(10): ${order_predict.calculate_total():.2f}")

# 2. Test Section 2.4 (StudentDiscount and Association)
print("\n--- Section 2.4 Test ---")
student_discount = StudentDiscount()

order2 = Order("ORD-002", student_discount) # Pass via constructor
order2.add_order_line(mouse, 2) # 100
print(f"Order2 total (student): ${order2.calculate_total():.2f}")

# Prove association: order3 can share the exact same student_discount object
order3 = Order("ORD-003")
order3.set_discount(student_discount)
order3.add_order_line(laptop, 1) 
print(f"Order3 total (same discount object): ${order3.calculate_total():.2f}")

# Prove the discount is independent of the order
print(f"Shared discount object is still usable: {student_discount.apply(100)}")