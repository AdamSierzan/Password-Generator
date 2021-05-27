import Password_gen
import random
from tkinter import font
from tkinter.constants import WORD
from typing import Text
import pygame
import random
import string
import tkinter.messagebox


root = tkinter.Tk()
root.geometry("480x460")
root.title("Password Generator")

background_image = tkinter.PhotoImage(file='hacker.png')
background_label = tkinter.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tkinter.Frame(root, bg='green', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
print("gola")


entry = tkinter.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tkinter.Button(frame, text="Generate", font=40, command=lambda: Password_gen.new_password)
button.place(relx=0.7,  relheight=1, relwidth=0.3)

lower_frame = tkinter.Frame(root, bg='green', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.65, anchor='n')


root.mainloop()

