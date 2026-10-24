from product import Product

class Inventory:
    def __init__(self):
        self.__products = []

    def get_products(self):
        return self.__products

    def is_empty(self):
        return len(self.__products) == 0

    def count(self):
        return len(self.__products)

    # CRUD
    def add_product(self, product):
        """Add a Product to the inventory. Returns False if ID exists."""
        if self.search_product(product.get_product_id()) is not None:
            print(f"Error: Product ID {product.get_product_id()} already exists.")
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id):
        """Return a Product by ID, or None."""
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def update_stock(self, product_id, new_stock):
        """Update the stock of a product by ID."""
        product = self.search_product(product_id)
        if product is None:
            print("Product not found.")
            return False
        return product.set_stock(new_stock)

    # display
    def display_all(self):
        """Print all products."""
        if self.is_empty():
            print("Inventory is empty.")
            return

        print("Current Inventory")
        print("-" * 48)
        for product in self.__products:
            product.display_information()
        print("-" * 48)


    def to_list_of_dicts(self):
        """Convert to list of dicts for JSON saving."""
        return [product.to_dict() for product in self.__products]

    def load_from_list_of_dicts(self, data):
        """Replace inventory contents with products from a list of dicts."""
        self.__products = [Product.from_dict(item) for item in data]