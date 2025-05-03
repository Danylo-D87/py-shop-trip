from app.car import Car
from app.customer import Customer
from app.shop import Shop

import json


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

        fuel_price = config["FUEL_PRICE"]

        shops = [Shop(**shop_data) for shop_data in config["shops"]]

        customers = []
        for customer_data in config["customers"]:
            car_data = customer_data.pop("car")
            car = Car(**car_data)
            customer = Customer(**customer_data, car=car)
            customers.append(customer)

        for customer in customers:
            print(f"{customer.name} has {customer.money} dollars")
            trip_options = []

            for shop in shops:
                total_trip_cost = (
                    customer.calculate_trip_cost(shop.location, fuel_price) * 2 +
                    shop.calculate_product_cart_cost(customer.product_cart)
                )
                print(f"{customer.name}'s trip to the {shop.name} costs {total_trip_cost:.2f}")
                if total_trip_cost <= customer.money:
                    trip_options.append((total_trip_cost, shop))

            if trip_options:
                trip_options.sort(key=lambda x: x[0])
                cheapest_shop = trip_options[0][1]

                print(f"{customer.name} rides to {cheapest_shop.name}")
                customer.location = cheapest_shop.location
                cheapest_shop.generate_receipt(customer)

                print(f"{customer.name} rides home")
                fuel_to_shop = customer.calculate_trip_cost(cheapest_shop.location, fuel_price)
                total_purchase_cost = cheapest_shop.calculate_product_cart_cost(customer.product_cart)
                customer.money -= (fuel_to_shop * 2 + total_purchase_cost)
                print(f"{customer.name} now has {customer.money} dollars\n")
            else:
                print(f"{customer.name} doesn't have enough money to make a purchase in any shop\n")
