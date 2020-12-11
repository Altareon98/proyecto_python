#!C:\Users\alexi\AppData\Local\Programs\Python\Python39\python.exe

import cgi
import html
import os
from conexion import conn

cursor = conn.cursor()

print('Content-type: text/html\n')

form = cgi.FieldStorage()

query = """SELECT * FROM alumno"""
cursor.execute(query)
result = cursor.fetchall()
contenido = "["
for row in result:
    ncontrol = row[0]
    nombre = row[1]
    fnacimiento = str(row[2])
    telefono = row[3]
    contenido = contenido + '{"Num_Control": "' + ncontrol + '","Nombre": "' + nombre + '","Fecha_Nacimiento": "' + fnacimiento + '","Telefono": "' + telefono + '"},'
        
contenido = contenido[:-1]
contenido = contenido + "]"
cursor.close()
conn.close()

archivo = open("alumnos.json", 'w')
archivo.write(contenido)
archivo.close()

if "alumnos.json" in os.listdir("."):
    print ("El archivo fue creado!")
else:
    print ("El archivo no fue creado!!!")


