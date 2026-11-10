from product import Product
from orderline import OrderLine


class Order:
    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def get_order_id(self) -> str:
        return self.__order_id

    def get_order_lines(self) -> list[OrderLine]:
        return self.__order_lines

    def add_order_line(self, product: Product, quantity: int) -> None:
        # create an OrderLine and add it to the order
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, index: int) -> bool:
        # remove an OrderLine by index. Removing from this Order destroys the OrderLine (composition)
        if 0 <= index < len(self.__order_lines):
            removed = self.__order_lines.pop(index)
            print(f"Order line for '{removed.get_product().get_name()}' removed from Order {self.__order_id}.")
            return True
        print(f"Error: Order line index {index} out of range.")
        return False

    def calculate_total(self) -> float:
        # sum of all OrderLine subtotals.
        total = 0.0
        for line in self.__order_lines:
            total += line.calculate_subtotal()
        return total

    def display_information(self) -> None:
        # print the whole order
        print(f"Order ID: {self.__order_id}")
        print("-" * 60)
        if not self.__order_lines:
            print("  (no order lines)")
        for line in self.__order_lines:
            line.display_information()
        print("-" * 60)
        print(f"  TOTAL: ${self.calculate_total():.2f}")