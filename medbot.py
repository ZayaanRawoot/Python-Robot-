import robot as r1

class MedicalBot(r1.Robot):

    def __init__(self, name, color, healing_power=25):
        super().__init__(name, color)
        self.healing_power = healing_power
    
    def heal(self,other_bot):

        if self.battery >= self.healing_power:
            other_bot.battery += self.healing_power
            
            print(f"{self.name} has battery: {self.battery}\n {other_bot.name} has battery: {other_bot.battery}")

            self.battery -= self.healing_power

            print(f"{self.name} has healed {other_bot.name} with {self.healing_power} \n {other_bot.name} now has {other_bot.battery}")
            pass # we can heal
        else:
            print(f"{self.name}  doesn't have enough power to heal")
