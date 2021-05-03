import time
import random
def simulator(x):
    if x == 'n':
        print("Dice not Rolled")
        time.sleep(1)
        print("----GAME OVER----")
    elif x == 'r':
        answer = random.randint(1,6)
        print("Dice Rolled -> "+str(answer))

print("Dice Rolling Simulator")
time.sleep(1)
x = input("Type 'r' for Roll and 'n' for No Roll: \n")
time.sleep(1)
simulator(x)
