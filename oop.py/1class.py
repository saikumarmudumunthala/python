# class is a template/blue-print for real-world entities
# class is a user-degined datatypes
# integerdatatype -->Int
#                    float
#                    bool
#                    str

# it is an user defined datatype this is a datatype which tou can create by yours


# creating the first class

class Phone:
    def make_call(self):
        print("making phone call")
    def play_game(self):
        print("playing games")    

p1 = Phone()

p1.make_call()
p1.play_game()

#Adding parameters in to class

class Phone:
    def set_color(self,color):
        self.color=color

    def set_cost(self,cost):
        self.cost=cost

    def show_color(self):
        return self.color

    def show_cost(self):
        return self.cost

    def make_call(self):
        print("making phone call")

    def play_games(self):
        print("play gmaes")
                

p2 = Phone()      
p2.set_color("blue")
p2.set_cost("100000")
sai=p2.show_color()
print(sai)
p2.set_cost("100000")
sai1=p2.show_cost()
print(sai1)
