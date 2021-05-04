#UNFINISHED PROJECT
from tkinter import *
from PIL import ImageTk, Image
import random
import time
# creating tkinter window
root = Tk()
root.geometry('500x500')
root.resizable(0,0)
root.title("Rock Paper Scissors (by - zoot/nix)")

icon = PhotoImage(file = 'rps_icon.png')
root.iconphoto(False, icon)

Label(root, text = "Let's Play Rock-Paper-Scissors", font = "Calibri 15 bold").place(x = 120, y = 40)

def rock_in():
    user_choice = 'rock'
    if pc_choice == 'rock':
        Label(root, text = ''+user_choice.capitalize()+' vs '+pc_choice.capitalize(), font = 'Calibri 15').place(x = 190, y = 300)
        Label(root, text = 'Match Tied', font = 'Calibri 15 bold').place(x = 190, y = 350)
    elif pc_choice == 'paper':
        Label(root, text = ''+user_choice.capitalize()+' vs '+pc_choice.capitalize(), font = 'Calibri 15').place(x = 190, y = 300)
        Label(root, text = 'Computer Won!', font = 'Calibri 15 bold').place(x = 190, y = 350)
    elif pc_choice == 'scissors':
        Label(root, text = ''+user_choice.capitalize()+' vs '+pc_choice.capitalize(), font = 'Calibri 15').place(x = 190, y = 300)
        Label(root, text = 'You Won!', font = 'Calibri 15 bold').place(x = 190, y = 350)


def paper_in():
    user_choice = 'paper'
    if pc_choice == 'paper':
        Label(root, text = ''+user_choice.capitalize()+' vs '+pc_choice.capitalize(), font = 'Calibri 15').place(x = 190, y = 300)
        Label(root, text = 'Match Tied', font = 'Calibri 15 bold').place(x = 190, y = 350)
    elif pc_choice == 'scissors':
        Label(root, text = ''+user_choice.capitalize()+' vs '+pc_choice.capitalize(), font = 'Calibri 15').place(x = 190, y = 300)
        Label(root, text = 'Computer Won!', font = 'Calibri 15 bold').place(x = 190, y = 350)
    elif pc_choice == 'rock':
        Label(root, text = ''+user_choice.capitalize()+' vs '+pc_choice.capitalize(), font = 'Calibri 15').place(x = 190, y = 300)
        Label(root, text = 'You Won!', font = 'Calibri 15 bold').place(x = 190, y = 350)


def scissors_in():
    user_choice = 'scissors'
    if pc_choice == 'scissors':
        Label(root, text = ''+user_choice.capitalize()+' vs '+pc_choice.capitalize(), font = 'Calibri 15').place(x = 190, y = 300)
        Label(root, text = 'Match Tied', font = 'Calibri 15 bold').place(x = 190, y = 350)

    elif pc_choice == 'rock':
        Label(root, text = ''+user_choice.capitalize()+' vs '+pc_choice.capitalize(), font = 'Calibri 15').place(x = 190, y = 300)
        Label(root, text = 'Computer Won!', font = 'Calibri 15 bold').place(x = 190, y = 350)

    elif pc_choice == 'paper':
        Label(root, text = ''+user_choice.capitalize()+' vs '+pc_choice.capitalize(), font = 'Calibri 15').place(x = 190, y = 300)
        Label(root, text = 'You Won!', font = 'Calibri 15 bold').place(x = 190, y = 350)

#creating button with scissor image
scissors_image = Image.open("scissor.png")
scissors_image_resized = scissors_image.resize((90,90),  Image.ANTIALIAS)
scissors = ImageTk.PhotoImage(scissors_image_resized)
scissors_btn = Button(root, borderwidth = 0, image = scissors, command = scissors_in).place(x = 200, y = 90)

#creating button with paper image
paper_image = Image.open("paper.png")
paper_image_resized = paper_image.resize((90,90),  Image.ANTIALIAS)
paper = ImageTk.PhotoImage(paper_image_resized)
paper_btn = Button(root, borderwidth = 0, image = paper, command = paper_in).place(x = 130, y = 190)

#creating button with rock image
rock_image = Image.open("rock.png")
rock_image_resized = rock_image.resize((90,90),  Image.ANTIALIAS)
rock = ImageTk.PhotoImage(rock_image_resized)
rock_btn = Button(root, borderwidth = 0, image = rock, command = rock_in).place(x = 270, y = 190)

choice_list = ['rock', 'scissors','paper']
pc_choice = random.choice(choice_list)


root.mainloop()
