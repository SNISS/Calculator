from os import system
from time import sleep
from types import TracebackType
import pyfiglet

def banner():
    banner = pyfiglet.figlet_format("Calculator")
    print(banner)

while True:
    
        sleep(2)
        system("clear")
        banner()
        print("Choose the options:\n[1]Multiply\n[2]Factor\n[3]Exit\n[4]sum\n[5]addition\n[6]Rest of division\n[7]Division\n")
        user = int(input("Choice: "))
        if user == 1:
        
           n1 = float(input("Choice a number: "))
           n2 = float(input("Choie another number: "))
           print(f"The result is {n1*n2}")
        elif user == 2:
            n1 = float(input("Choice a number: "))
            n2 = float(input("Choie another number: "))
            print(f"The result is {n1**n2}")
        elif user == 3:
            print("Goodbye")
            exit()
        elif user == 4: 
            n1 = float(input("Choice a number: "))
            n2 = float(input("Choie another number: "))
            print(f"The result is {n1 + n2}")
        elif user == 5:
            n1 = float(input("Choice a number: "))
            n2 = float(input("Choie another number: "))
            print(f" The result is {n1 - n2}")
        elif user == 6:
            n1 = float(input("Choice a number: "))
            n2 = float(input("Choie another number: "))
            print(f"The result is {n1 // n2}")
        elif user == 7:
            n1 = float(input("Choice a number: "))
            n2 = float(input("Choie another number: "))
            print(f"The result is {n1/n2}")
        else: 
            print("Option not found")
    