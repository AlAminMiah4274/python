from users import Rider, Driver
from ride import Ride, RideRequest, RideMatching, RideSharing
from vehicle import Car, Bike 


niye_jao = RideSharing("Niye Jao")

rahim = Rider("Rahim", "rahim@khan.com", 35746874, "uttara", 1200)
niye_jao.add_rider(rahim)

kolim_uddin = Driver("Kolim Uddin", "kolim@uddin.com", 54787921, "ariport")
niye_jao.add_driver(kolim_uddin)

rahim.request_ride(niye_jao, "gulshan", "car")
rahim.show_current_ride()

kolim_uddin.reach_destination(rahim.current_ride)


print(niye_jao)