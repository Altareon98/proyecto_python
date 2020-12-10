#!C:\Users\alexi\AppData\Local\Programs\Python\Python39\python.exe

import tkinter as tk
from tkinter import filedialog
#from alumno import vaciarTabla

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

print("Content-type:text/html\r\n\r\n")

f = open(file_path, "r")
contenido = f.read()

#vaciarTabla()

print(contenido)