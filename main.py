import os
import time
from colorama import Fore, Back, Style, init
from random import *
import pyfiglet

T = "BiteFoundUrDad"
ASCII_art_1 = pyfiglet.figlet_format(T)
print(ASCII_art_1)
init()
print("by Opale#0001")
print(Fore.GREEN+"")
input("start ?")

def localisation_dad():
    eeee = 10
    aecrirearr = "█"
    aecrirearr3 = ""
    tipographtipo =0
    while tipographtipo < eeee :

        time.sleep(1)
        aecrirearr2 = aecrirearr * randint(1,6)
        aecrirearr3 += aecrirearr2
        os.system("cls")
        print(Fore.WHITE+"locate your dad")
        print(Fore.GREEN+aecrirearr3)
        tipographtipo += 1
        print(Fore.WHITE+"time estimate : ", eeee ,"s :",tipographtipo)
    os.system("cls")

localisation_dad()


print(Fore.YELLOW+"LOL your dad never come back with the milk")
print("X:",random()80, "Y:",random()80)

input()
input()
