from datetime import datetime
from vehicle import Car, Bike


class Ride:
	def __init__(self, start_location, end_location, vehicle_type):
		self.start_location = end_location
		self.end_location = end_location
		self.rider = None
		self.driver = None
		self.start_time = None
		self.end_time = None
		self.estimated_fare = self.calculate_fare(vehicle_type)
		self.vehicle_type = vehicle_type


	def set_driver(self, driver):
		self.driver = driver


	def start_ride(self):
		self.start_time = datetime.now()


	def end_ride(self):
		self.end_time = datetime.now()
		self.rider.wallet -= self.estimated_fare
		self.driver.wallet += self.estimated_fare


	def calculate_fare(self, vehicle):
		distance = 10

		fare_per_km = {
			"car": 30,
			"bike": 20,
			"cng": 25
		}

		return distance * fare_per_km.get(vehicle)


	def __repr__(self):
		return f"Ride detail: started {self.start_location} to {self.end_location}"



class RideRequest:
	def __init__(self, rider, end_location):
		self.rider = rider 
		self.end_location = end_location



class RideMatching:
	def __init__(self, drivers):
		self.available_drivers = drivers


	def find_driver(self, ride_request, vehicle_type):
		if len(self.available_drivers) > 0:
			print("Looking for driver .....")

			driver = self.available_drivers[0]

			if vehicle_type == "car":
				vehicle = Car("car", "1254BCD", 500)
			elif vehicle_type == "bike":
				vehicle = Bike("bike", "4781ABD", 420)

			ride = Ride(ride_request.rider.current_location, ride_request.end_location, vehicle)
			driver.accept_ride(ride)

			return ride



class RideSharing:
	def __init__(self, company_name):
		self.company_name = company_name
		self.riders = []
		self.drivers = []
		self.rides = []


	def add_rider(self, rider):
		self.riders.append(rider)


	def add_driver(self, driver):
		self.drivers.append(driver)


	def __repr__(self):
		return f"Company name: {self.company_name} with riders: {len(self.riders)} and driver: {len(self.drivers)}"