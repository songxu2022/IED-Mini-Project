# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk

window = tk.Tk()

window.title('Ball Launcher')
window.geometry('500x300')

var1 = tk.StringVar()
l = tk.Label(window, bg='green', fg='yellow',font=('Arial', 12), width=10, textvariable=var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)
    newwindow = tk.Toplevel(window)
    newwindow.geometry('500x300')
    newwindow.title("Spring 1")
    canvas = tk.Canvas(newwindow, bg='green', height=900, width=900)
    image_file = ".\\"
    if(value == "Spring1"):
        image_file = tk.PhotoImage(file="spring1.gif")
    if(value == "Spring2"):
        image_file = tk.PhotoImage(file="spring2.gif")
    if(value == "Spring3"):
        image_file = tk.PhotoImage(file="spring3.gif")

    image = canvas.create_image(0, 0, anchor='nw',image=image_file)
    canvas.pack()
    newwindow.mainloop()
    
    
b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
b1.pack()

lb = tk.Listbox(window)
list_items = ["Spring1", "Spring2", "Spring3"]
for item in list_items:
    lb.insert('end', item)  # 
lb.pack()

window.mainloop()