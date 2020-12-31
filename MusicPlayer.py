#importing necessary modules
import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

#creating application window
musicplayer = tkr.Tk()

#Setting the title
musicplayer.title("Musica Space")

#setting the Dimensions
musicplayer.geometry("450x350")

#Asking for Music Directory
directory = askdirectory()

#Setting Music Directory to Current Working Directory
os.chdir(directory)

#Creating Our songlist
#os.listdir() returns the list containing the names of the entries in the directory given by user
songlist = os.listdir()

#Creating the Playlist
playlist = tkr.Listbox(musicplayer, font="cambria 14 bold" , bg="white", selectmode=tkr.SINGLE)

#Adding songs from songlist to playlist
for item in songlist:
    pos=0
    playlist.insert(pos,item)
    pos = pos + 1

#initializing Modules
pygame.init()
pygame.mixer.init()

playlist.pack(fill="both",expand="yes")


# Function for play button
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

# Function for stop button
def stop():
    pygame.mixer.music.stop()

# Function for pause button
def pause():
    pygame.mixer.music.pause()

# Function for resume button
def resume():
    pygame.mixer.music.unpause()

#Creating Buttons
Button_play = tkr.Button(musicplayer, height=3, width=5, text="Play", font="cambria 14 bold italic", command=play, bg ="black", fg="white")
Button_stop = tkr.Button(musicplayer, height=3, width=5, text="stop", font="cambria 14 bold italic", command=stop, bg ="black", fg="white")
Button_pause = tkr.Button(musicplayer, height=3, width=5, text="Pause", font="cambria 14 bold italic", command=pause, bg ="black", fg="white")
Button_resume = tkr.Button(musicplayer, height=3, width=5, text="resume", font="cambria 14 bold italic", command=resume, bg ="black", fg="white")

Button_play.pack(fill='x')
Button_stop.pack(fill='x')
Button_pause.pack(fill='x')
Button_resume.pack(fill='x')


var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font="cambria 12 bold italic", textvariable= var)

songtitle.pack()
musicplayer.mainloop()