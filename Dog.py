class Dog:

    dogName=None
    dogHeight=None
    dogColor=None

    def barking(self):
        print("dog is barking:")
    
    def running(self,fghj):
        print("This dog is ruuning at the speed of " + str(fghj) + " km/h")

    def specification(self):
        print("Dog Name is:"+ self.dogName)
        print("Dog Height is:"+ self.dogHeight)
        print("Dog Color is:"+ self.dogColor)

def start():
    print("this is main method")

if __name__=="__main__":
    start()

    germandog=Dog()

    germandog.dogColor="black"
    germandog.dogHeight="6"
    germandog.dogName="Rocky"

    germandog.running(9)
    germandog.barking()
    germandog.specification()
