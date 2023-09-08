class Parent():
    def assign_name(self,name):
        self.name = name

    def show_name(self):
        return self.name

class child(Parent):
    def assign_age(self,age):
        self.age = age

    def show_age(self):
        return self.age()

class Grandchild(child):
    def assign_gender(self,gender):
        self.gender = gender

    def show_gender(self):
        return self.name


g1 = Parent()
g2 = child()
g3 = Grandchild()


g1.assign_name("saikumar")
g2.assign_age("25")
g3.assign_gender("Male")

g1.show_name()
g2.show_age()
g3.show_gender()

        
