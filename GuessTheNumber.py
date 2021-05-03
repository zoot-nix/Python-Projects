import time
import random
print("----Welcome to Guess the Number!----")
time.sleep(2)
print("Rules:\n 1.For answering type the number (e.g. -> 4) \n 2.You have 10 tries only.")
time.sleep(2)
print("\nLet's Begin")
time.sleep(1)
chosen_number = random.randint(1,100)
c = 9
while c >= 0:
    c -= 1
    time.sleep(1)
    player_number = int(input("\nEnter your guess: "))
    if player_number == chosen_number:
        print("Congratulations, You WON!")
        break
    elif player_number > chosen_number:
        print("Your Guess is too high.")
    elif player_number <chosen_number:
        print("Your Guess is too low.")
if c <= 0:
    print("\n-----GAME OVER-----")
    print("The Number was:"+str(chosen_number))
