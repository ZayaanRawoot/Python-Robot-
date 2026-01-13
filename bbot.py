from robot import Robot as r
# import robot as r

class BattleBot(r):

    def __init__(self,name,color,weapon,attack_pwr = 50):
        super().__init__(name,color) #Uses Robot's __init__  
        self.weapon = weapon
        self.attack_power = attack_pwr   
    
    def __str__(self):
        return f"{self.name} has the {self.color}"

    def fight(self, enemy):
        if self.battery >= 20:
            enemy.battery -= self.attack_power
            self.battery -=20
            print(f"{self.name} attacks {enemy.name} with  a {self.weapon} \n {self.name} battery: {self.battery}\n {enemy.name} battery: {enemy.battery}")
            pass
        else:
            print(f"{self.name} is too weak to fight !")