import string
import random


class VehicleRegistry:

    def generate_vehicle_id(self, lenght):
        return ''.join(random.choices(string.ascii_uppercase, k=lenght))

    def generate_vehicle_license(self, id):
        return f'{id[:2]}-{"".join(random.choices(string.digits, k=2))}-{"".join(random.choices(string.ascii_uppercase, k=2))}'


class Application:

    def register_vehicle(self, brand):
        registry = VehicleRegistry()

        vehicle_id = registry.generate_vehicle_id(12)
        license_plate = registry.generate_vehicle_license(vehicle_id)

        catalogue_price = 0
        if brand == "Tesla Model 3":
            catalogue_price = 60000
        elif brand == "Volkswagen ID3":
            catalogue_price = 35000
        elif brand == "BMW 5":
            catalogue_price = 45000

        tax_percentage = 0.05
        if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
            tax_percentage = 0.02

        payable_tax = tax_percentage * catalogue_price

        print("Registration complete. Vehicle information:")
        print(f"Brand: {brand}")
        print(f"Id: {vehicle_id}")
        print(f"License plate: {license_plate}")
        print(f"Payable tax: {payable_tax}")


if __name__ == '__main__':
    
    app = Application()
    app.register_vehicle("BMW 5")