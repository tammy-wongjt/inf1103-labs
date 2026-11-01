class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock


    def update_stock(self, quantity):
        # update stock by adidng quantity
        if self.__stock + quantity < 0:
            print("Error: Stock cannot be negative.")
            return False
        self.__stock += quantity
        return True

    def set_stock(self, new_stock):
        # set the stock to a specific value (option 3)
        if new_stock < 0:
            print("Error: Stock cannot be negative.")
            return False
        self.__stock = new_stock
        return True

    def display_information(self):
        # Print the product's details
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")


    def to_dict(self):
        # convert to dict for JSON saving.
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

    @classmethod
    def from_dict(cls, data):
        # create a Product from a dict (for loading from JSON).
        return cls(data["id"], data["name"], data["price"], data["stock"])


class PhysicalProduct(Product):

    # add weight
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")


class DigitalProduct(Product):

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_download_size(self):
        return self.__download_size

    def display_information(self):
        super().display_information()
        print(f"Download size: {self.__download_size} MB")