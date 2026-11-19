from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float) -> None:
        self._percentage = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self._percentage / 100)

class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, discount_amount: float) -> None:
        self._threshold = threshold
        self._discount_amount = discount_amount

    def apply(self, total: float) -> float:
        if total >= self._threshold:
            return total - self._discount_amount
        return total

# 2.4 Fourth strategy (StudentDiscount)
class StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.95  # 5% off