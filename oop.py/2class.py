class Employee:
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def show_details(self):
        print("The name of Employee is",self.name)    
        print("The name of Employee is",self.age)
        print("The name of Employee is",self.salary)
        print("The name of Employee is",self.gender)

e1 = Employee('sam',25,80000,'male')

e1.show_details()