import time
from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("YouTube Video Downloader (by - zoot/nix)")

icon = PhotoImage(file = 'yt.png')
root.iconphoto(False, icon)

Label(root, text = "YouTube Video Downloader", font = "Helvetica 20 ",).pack()

link = StringVar() #to store th yt video link
Label(root, text = "↓ Paste Link Here ↓", font = "Helvetica 15 ").place(x = 160, y = 60)
enter_link = Entry(root, width = 70, textvariable = link).place(x = 32, y = 100)

def vid_downloader_high():
    url = YouTube(str(link.get()))#get() to fetch link from link variable
    video = url.streams.get_highest_resolution()#to get video in highest resolution
    video.download('Downloads')#creates a 'Downloads' folder in the current working directory and saves video within it
    Label(root, text = "Video Downloaded ✓", font = 'Helvetica 10').place(x = 190, y = 210)

def vid_downloader_current():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download('Downloads')
    Label(root, text = "Video Downloaded", font = 'Helvetica 10').place(x = 190, y = 210)

Button(root, text = "Current Resolution Download", font = "Helvetica 9 bold",fg = 'white', bg = 'red', padx = 2, command = vid_downloader_current).place(x = 60, y =170)

Button(root, text = "High Resolution Download", font = "Helvetica 9 bold",fg = 'white', bg = 'black', padx = 2, command = vid_downloader_high).place(x = 260, y =170)

root.mainloop()
