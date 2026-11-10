from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier
from product import Product

class Inventory:
    def __init__(self) -> None:
        self.__products: list[Product] = []

    def get_products(self) -> list[Product]:
        return self.__products

    def is_empty(self) -> bool:
        return len(self.__products) == 0

    def count(self) -> int:
        return len(self.__products)

    # CRUD
    def add_product(self, product: Product) -> bool:
        """Add a Product to the inventory. Returns False if ID exists."""
        if self.find_product(product.get_product_id()) is not None:
            print(f"Error: Product ID {product.get_product_id()} already exists.")
            return False
        self.__products.append(product)
        return True

    # remove product by ID
    def remove_product(self, product_id: str) -> bool:
        product = self.find_product(product_id)
        if product is None:
            print(f"Product {product_id} not found.")
            return False
        self.__products.remove(product)
        print(f"Product {product_id} removed from inventory.")
        return True

    def find_product(self, product_id: str) -> Product | None:
        """Return a Product by ID, or None."""
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def update_stock(self, product_id: str, new_stock: int) -> bool:
        """Update the stock of a product by ID."""
        product = self.find_product(product_id)
        if product is None:
            print("Product not found.")
            return False
        return product.set_stock(new_stock)

    # display
    def display_all(self) -> None:
        """Print all products."""
        if self.is_empty():
            print("Inventory is empty.")
            return

        print("Current Inventory")
        print("-" * 48)
        for product in self.__products:
            product.display_information()
        print("-" * 48)


    def to_list_of_dicts(self) -> list[dict]:
        """Convert to list of dicts for JSON saving."""
        return [product.to_dict() for product in self.__products]


    def load_from_list_of_dicts(self, data: list[dict]) -> None:
        """Replace inventory contents with products from a list of dicts."""
        self.__products = []
        for item in data:
            supplier_data = item["supplier"]
            supplier = Supplier(
                supplier_data["supplier_id"],
                supplier_data["name"],
                supplier_data["contact_email"],)
                

            product_type = item.get("type", "physical")  # default for old data
            if product_type == "physical":
                p = PhysicalProduct(item["id"], item["name"], item["price"], item["stock"], supplier, item["weight"])
            elif product_type == "digital":
                p = DigitalProduct(item["id"], item["name"], item["price"], item["stock"], supplier, item["download_size"])
            else:
                print(f"Warning: unknown product type '{product_type}' — skipped")
                continue
            self.__products.append(p)