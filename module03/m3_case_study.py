# Define the SuperClass vehivle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Define the subClass Automobile
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type) # calls the vehicle constructor`
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Get User Input
vehicle_type = input("Enter type of vehicle (car, truck, van, boat, etc): ")
year = input(f"Enter the year of the {vehicle_type}: ")
make = input(f"Enter the make of the {vehicle_type}: ")
model = input(f"Enter the model of the {vehicle_type}: ")
doors = input("Enter number of doors (2 or 4): ")
roof = input("Enter type of roof (solid or sun roof): ")

# Create an instance of Automobile
my_car = Automobile(vehicle_type, year, make, model, doors, roof)

# Display the output
print("\nHere is the information you entered:")
print(f"Vehicle type: {my_car.vehicle_type}")
print(f"Year: {my_car.year}")
print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")
print(f"Number od doors: {my_car.doors}")
print(f"Type of roof: {my_car.roof}")