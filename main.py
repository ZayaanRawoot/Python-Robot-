# import robot as t

from robot import Robot
from bbot import BattleBot
import medbot 

bot1 = BattleBot("Megatron","Black","Laser Gun",60)
bot2 = BattleBot("Optimus","Blue","Sword")
med_bot = medbot.MedicalBot("MedO02","white")


bot1.fight(bot2)
bot1.walk()
bot2.fight(bot1)

med_bot.heal(bot1)

