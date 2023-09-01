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