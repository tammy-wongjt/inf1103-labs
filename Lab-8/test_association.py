from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

# Set up a supplier
supplier = Supplier("S001", "Tammy", "twjt@gmail.com")

# Create products using that supplier
p1 = PhysicalProduct("P001", "Phone", 2000, 300, supplier, 0.5)
p2 = DigitalProduct("B001", "E-Book", 15.99, 999, supplier, 5.2)

print("--- Association Test ---")
print("Displaying products to show supplier details:")
p1.display_information()
p2.display_information()

print("\nChecking object references:")
print(f"p1 and p2 point to the same supplier object: {p1.get_supplier() is p2.get_supplier()}")

print("\nDeleting the 'supplier' variable to test independence:")
del supplier

# Even though the variable is deleted, the objects still hold references
print("Attempting to display product info after deleting the variable...")
p1.display_information()

print("\nDeleting p1 to test reverse independence:")
del p1

# p2 still holds the supplier, so it should still work
print(f"p2 still has its supplier: {p2.get_supplier().get_name()} ({p2.get_supplier().get_contact_email()})")