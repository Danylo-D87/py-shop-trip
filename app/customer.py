from dataclasses import dataclass
import math

from app.car import Car
#from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: list[str]
    location: list[int]
    money: float | int
    car: Car

    def calculate_trip_cost(self,
                            shop_location: list[int],
                            fuel_price: float
                            ) -> float:
        # розрахунок відстані
        x1, y1 = self.location
        x2, y2 = shop_location
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        res = self.car.fuel_cost(distance, fuel_price)
        return res

    def can_afford_trip(self,
                        shop_location: list[int],
                        fuel_price: float,
                        shop_name: str) -> bool:
        # Імпортуємо тут клас Shop для уникнення циклічного імпорту
        from app.shop import Shop

        cost_product_cart = shop_name.calculate_product_cart_cost(self.product_cart)
        cost_fuel = self.calculate_trip_cost(shop_location, fuel_price)

        if cost_fuel + cost_product_cart <= self.money:
            return True
        else:
            return False
