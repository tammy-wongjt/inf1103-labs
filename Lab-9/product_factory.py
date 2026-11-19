from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier


class ProductFactory:
    @staticmethod
    def create(
        product_type: str,
        product_id: str,
        name: str,
        price: float,
        stock_quantity: int,
        supplier: Supplier,
        *extra_args
    ) -> Product:
        """Create a product of the given type. 
        Extra args are passed to the subclass constructor (weight or download_size).
        """
        if product_type == "physical":
            weight = extra_args[0] if extra_args else 0.0
            return PhysicalProduct(product_id, name, price, stock_quantity, supplier, weight)
        elif product_type == "digital":
            download_size = extra_args[0] if extra_args else 0.0
            return DigitalProduct(product_id, name, price, stock_quantity, supplier, download_size)
        else:
            raise ValueError(f"Unknown product type: {product_type}")