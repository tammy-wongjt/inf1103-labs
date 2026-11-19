from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier) -> None:
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if stock < 0:
            raise ValueError("Stock quantity cannot be negative.")
        
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.__supplier: Supplier = supplier

    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def get_supplier(self) -> Supplier:
        return self.__supplier

    def update_stock(self, quantity: int) -> bool:
        # update stock by adidng quantity
        if self.__stock + quantity < 0:
            print("Error: Stock cannot be negative.")
            return False
        self.__stock += quantity
        return True

    def set_stock(self, new_stock: int) -> bool:
        # set the stock to a specific value (option 3)
        if new_stock < 0:
            print("Error: Stock cannot be negative.")
            return False
        self.__stock = new_stock
        return True

    def display_information(self) -> None:
        # Print the product's details
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")
        print(f"Supplier: {self.__supplier.get_name()}, {self.__supplier.get_contact_email()}")

    def to_dict(self) -> dict:
        # convert to dict for JSON saving.
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.__supplier.to_dict()
        }


    @abstractmethod
    def get_fulfilment_info(self) -> str:
        # returns a message describing how the product is fulfilled (from the child)
        pass
