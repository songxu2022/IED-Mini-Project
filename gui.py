# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk

window = tk.Tk()

window.title('Ball Launcher')
window.geometry('500x300')


l = tk.Label(window, text ='Choose a spring', bg='white', fg='black',font=('Arial', 12), width=20)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    newwindow = tk.Toplevel(window)
    newwindow.geometry('500x300')
    newwindow.title(value)
    canvas = tk.Canvas(newwindow, bg='green', height=900, width=900)
    image_file = ".\\"
    if(value == "Spring1"):
        image_file = tk.PhotoImage(file="spring1.png")
    if(value == "Spring2"):
        image_file = tk.PhotoImage(file="spring2.png")
    if(value == "Spring3"):
        image_file = tk.PhotoImage(file="spring3.png")

    image = canvas.create_image(0, 0, anchor='nw',image=image_file)
    canvas.pack()
    newwindow.mainloop()
    
    


lb = tk.Listbox(window)
list_items = ["Spring1", "Spring2", "Spring3"]
for item in list_items:
    lb.insert('end', item)  # 
lb.pack()

def  go():
    print(entry1.get())
    
l = tk.Label(window, text ='Enter the distance', bg='white', fg='black',font=('Arial', 12), width=20)
l.pack()

entry1=tk.Entry(window,width=50,bg="white",fg="black")

entry1.pack()

b1 = tk.Button(window, text='generate result', width=15, height=2, command=print_selection)
b1.pack()

window.mainloop()