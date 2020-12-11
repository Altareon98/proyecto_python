#!C:\Users\alexi\AppData\Local\Programs\Python\Python39\python.exe

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

print('Content-type: text/html\n')

f = open(file_path, "r")
contenido = f.read()


print(contenido)