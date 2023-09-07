class Vehicle:
    def __init__(self,milage,cost):
        self.milage = milage
        self.cost = cost

    def show_details(self):
        print("milage is",self.milage)
        print("cost is",self.cost)

class Car(Vehicle):
    def __int__(self,milage,cost,tyres,horsepower):
        super().__init__(milage,cost)
        self.tyres = tyres
        self.horsepower = horsepower
        

    def show_car_details(self):
        print("number of tyres are",self.tyres)
        print("the horsepower",self.horsepower)

c1 = Car(10,5000000,4,1200)
c1.show_details()
c1.show_car_details()                        