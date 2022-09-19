# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 17:36:56 2022

@author: PC_RC
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.minsize(650, 650)
root.maxsize(650, 650)

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))

label_file_name = Label(root, text="File Name", bg = "seashell3")
label_file_name.place(relx = 0.38, rely = 0.03, anchor = CENTER)

input_file_name = Entry(root)
input_file_name.place(relx = 0.52, rely = 0.03, anchor = CENTER)

my_text = Text(root, height = 35, width = 80)
my_text.place(relx = 0.5, rely = 0.55, anchor = CENTER)

save_button = Button(root, image = save_img, text = "SaveFile", cursor = "star")
save_button.place(relx = 0.10, rely = 0.03, anchor = CENTER)

exit_button = Button(root, image = exit_img, text = "ExitFile", cursor = "star")
exit_button.place(relx = 0.15, rely = 0.03, anchor = CENTER)






open_button = Button(root, image = open_img, text = "OpenFile", cursor = "star")
open_button.place(relx = 0.05, rely = 0.03, anchor = CENTER)

root.mainloop()