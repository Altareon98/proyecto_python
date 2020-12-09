#!C:\Users\alexi\AppData\Local\Programs\Python\Python39\python.exe
import tableData as td
import json
import cgitb
cgitb.enable()

print("\n\n\n\n")

rawData = td.data
nControl = rawData[0][1]
nombres = rawData[1][1]
fNacimientos = rawData[2][1]
telefonos = rawData[3][1]

cuenta = len(nControl)
alumnos = []

for i in range(3):
    alumno = {
        "Num_Control": nControl[i], 
        "Nombre": nombres[i],
        "Fecha_Nacimiento": fNacimientos[i],
        "Telefono": telefonos[i]
    }
    alumnos.append(alumno)

b = json.dumps(alumnos)

with open("Sample.json", "w") as p:
    json.dump(alumnos, p)