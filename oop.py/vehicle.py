class Vehicle:
    def __init__(self, milage, cost):
        self.milage = milage
        self.cost = cost

    def show_details(self):
        print("Milage is", self.milage)
        print("Cost is", self.cost)

class Car(Vehicle):
     def __init__(self, milage, cost, tyres, horsepower):
         super().__init__(milage, cost)
         self.tyres = tyres
         self.horsepower = horsepower
        

     def show_car_details(self):
        print("Number of tyres are", self.tyres)
        print("The horsepower", self.horsepower)
        
c1 = Car(10, 5000, 4, 1200)

c1.show_car_details()
c1.show_details()


