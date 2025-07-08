#class Car:
#    brand: "VW"
#    color: "Black"
#from test.test_login import befor_and_after_tests


#Create object of the class
#car1 = Car()
#print(car1.brand)

#car2 = Car()
#print(car2.brand)

# init constructor, self -> object
class Vehicle:
    def __init__(self, brand, doors, wheels=4):
        self.brand = brand
        self.doors = doors
        self.wheels = wheels
    #methods inside the class, self is argument
    def car_greeting(self, locat_slang):
        print(f" {locat_slang} Hi, I am your new car. My name is  {self.brand} . I have {self.wheels} wheels.")

veh1 = Vehicle("VW", 2)
print(veh1.brand, veh1.doors, veh1.wheels)
veh1.car_greeting("Ja")

veh2 = Vehicle("Merzedes", 6)
print(veh1.brand, veh1.doors, veh1.wheels)