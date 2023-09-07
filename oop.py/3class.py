# Inheritance in python:-
# with inheritance one class can derive the properties of another class

class Vehicle:
   def __init__(self,milage,cost):
       self.milage = milage
       self.cost = cost

   def show_details(self):
       print("milage of vehicle is",self.milage)
       print("cost of vehicle is",self.cost)

v1 = Vehicle(50,50000)
v1.show_details()            

class Car:
    def __init__(self,milage,cost):
       self.milage = milage
       self.cost = cost

    def show_Car_details(self):
        print("car milage of vehicle is",self.milage)
        print("car cost of vehicle is",self.cost)
        
c1 = Car(7,600000)
c1.show_Car_details()        