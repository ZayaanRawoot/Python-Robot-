# Object-Oriented Programming(OOP)

class Robot:
    """Blueprint to make a robot"""
    
    def __init__(self,name,color):
        """init = Robot's birth (sets up its properties)"""  
        self.name = name 
        self.color = color
        self.battery = 100 # Starts with full battery

    # Methods = Actions the robot can do
    def walk(self):
        if self.battery >= 10:
            self.battery -= 10
            print(f"{self.name} is walking and battery is {self.battery}")
        else:
            print(f"{self.name} is out of battery")
    
    def recharge(self):
        self.battery = 100
        print(f"{self.name} is fully charged") 