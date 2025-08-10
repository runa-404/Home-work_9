# Домашня: # Створи код де при натисканні на кнопку рамка навколо твоєї кнопки # буде міняти свій колір на рандомний зі списку рандомних хекс кольорів.

import tkinter as tk
import random

colors = ["blue", "red", "yellow"]
def change_color():
    Frame1.config(bg=random.choices(colors))

root = tk.Tk()
Frame1 = tk.Frame(root, width=200, height=400)

Butto1 = tk.Button(root, text=("Натисни на мене щоб змінити колір"), command=change_color)

Frame1.pack()
Butto1.pack()

root.mainloop()
