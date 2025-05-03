from app.customer import Customer

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    def calculate_product_cart_cost(self,
            product_cart: list[str]
            ) -> int | float:
        cost = 0
        for product, count_product in product_cart.items():
            if product in self.products:
                cost += self.products[product] * count_product
            else:
                print(f"Product {product} is not available in {self.name}")
        return cost

    def generate_receipt(self, customer: Customer) -> None:

        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        total_cost = self.calculate_product_cart_cost(customer.product_cart)

        print(f"Date: {current_time}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for product, count_product in customer.product_cart.items():
            if product in self.products:
                print(f"{count_product} {product} for {self.products[product] * count_product} dollars")

        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
