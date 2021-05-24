import tkinter
import random
from tkinter import font
from tkinter.constants import WORD
from typing import Text
import pygame
import random
import string
# import password_generator
import tkinter.messagebox


root = tkinter.Tk()
root.geometry("480x460")
root.title("Password Generator")


frame = tkinter.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')



entry = tkinter.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tkinter.Button(frame, text="Generate", font=40)
button.place(relx=0.7,  relheight=1, relwidth=0.3)

lower_frame = tkinter.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.65, anchor='n')



root.mainloop()
