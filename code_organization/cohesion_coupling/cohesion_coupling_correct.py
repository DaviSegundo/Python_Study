import string
import random
from dataclasses import dataclass


@dataclass
class VehicleInfo:
    brand: str
    catalogue_price: int
    electric: bool

    def compute_tax(self) -> float:
        """Compute the tax percentage.""" 
        # (default 5% of the catalogue price, except for electric cars where it is 2%)
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price

    def print(self) -> None:
        """Print information about vehicle info."""
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")


@dataclass
class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    def print(self) -> None:
        """Print information about vehicle."""
        print(f"Id: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()


@dataclass
class VehicleRegistry:

    vehicle_info = {}

    def add_vehicle_info(self, brand: str, electric: bool, catalogue_price: int) -> None:
        """Set vehicle information."""
        self.vehicle_info[brand] = VehicleInfo(
            brand=brand, electric=electric, catalogue_price=catalogue_price)

    def __init__(self) -> None:
        """Adding vehicle information to fill the class informations."""
        self.add_vehicle_info(brand="Tesla Model 3", electric=True, catalogue_price=60000)
        self.add_vehicle_info(brand="Volkswagen ID3", electric=True, catalogue_price=35000)
        self.add_vehicle_info(brand="BMW 5", electric=False, catalogue_price=45000)

    def generate_vehicle_id(self, lenght: int) -> str:
        """Generate vehicle id given a lenght."""
        return ''.join(random.choices(string.ascii_uppercase, k=lenght))

    def generate_vehicle_license(self, id: str) -> str:
        """Generate vehicle license given a id."""
        return f'{id[:2]}-{"".join(random.choices(string.digits, k=2))}-{"".join(random.choices(string.ascii_uppercase, k=2))}'

    def create_vehicle(self, brand: str):
        """Create a vehicle instance from a given brand."""
        # generate a vehicle id of length 12
        vehicle_id = self.generate_vehicle_id(lenght=12)

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        license_plate = self.generate_vehicle_license(id=vehicle_id)

        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])


class Application:

    def register_vehicle(self, brand: str):
        """Register a vehicle in the application."""
        # create a resgistry instance
        registry = VehicleRegistry()

        # create a vehicle
        return registry.create_vehicle(brand=brand)
         

if __name__ == '__main__':
    app = Application()
    vehicle = app.register_vehicle("BMW 5")
    vehicle.print()
