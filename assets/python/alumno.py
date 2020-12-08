#!C:\Users\alexi\AppData\Local\Programs\Python\Python39\python.exe

# Importar modulos de CGI
import cgi
import json
from mysql import connector as conexion

conn = conexion.connect(user='root', password='',host='localhost', database='veranos')
cursor = conn.cursor()

print("Content-type:text/html\r\n\r\n")

parametros = cgi.FieldStorage()
accion = parametros.getvalue('accion')

if accion:
    if accion == "SELECTALL":
        query = """SELECT * FROM alumno"""
        cursor.execute(query)
        result = cursor.fetchall()
        jsonArray = []

        for row in result:
            ncontrol = row[0]
            nombre = row[1]
            fnacimiento = row[2].strftime('%m/%d/%Y')
            telefono = row[3]
            jsonArray.append({"Num_Control": ncontrol, "Nombre":  nombre,"Fecha_Nacimiento": fnacimiento, "Telefono": telefono})
        
        cursor.close()
        conn.close()
        print(jsonArray)
        exit()
        
    if accion == "SELECTWHERE":
        numControl = parametros.getvalue('numControl')
        
        query = "SELECT * FROM alumno WHERE Num_Control = %s"
        values = [numControl]
        cursor.execute(query, values)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        print({"Num_Control": result[0], "Nombre":  result[1],"Fecha_Nacimiento": result[2].strftime('%m/%d/%Y'), "Telefono": result[3]})
        exit()
        
    if accion == "UPDATE":
        numControl = parametros.getvalue('numControl')
        nombre = parametros.getvalue('nombre')        
        fechaNacimiento = parametros.getvalue('fechaNacimiento')
        telefono = parametros.getvalue('telefono')
       
        query = "UPDATE alumno SET Nombre = %s, Fecha_Nacimiento = %s, Telefono = %s WHERE Num_Control = %s"
        values = [nombre, fechaNacimiento, telefono, numControl]
        cursor.execute(query, values)
        conn.commit()
        print(cursor.rowcount)
        cursor.close()
        conn.close()
        exit()
    
    if accion == "DELETE":
        numControl = parametros.getvalue('numControl')
        
        query = "DELETE FROM alumno WHERE Num_Control = %s"
        values = [numControl]
        cursor.execute(query, values)
        conn.commit()
        print(cursor.rowcount)
        cursor.close()
        conn.close()
        exit()
        
    if accion == "INSERT":
        numControl = parametros.getvalue('numControl')
        nombre = parametros.getvalue('nombre')        
        fechaNacimiento = parametros.getvalue('fechaNacimiento')
        telefono = parametros.getvalue('telefono')
       
        query = "INSERT INTO alumno VALUES (%s, %s, %s, %s)"
        values = [numControl, nombre, fechaNacimiento, telefono]
        cursor.execute(query, values)
        conn.commit()
        print(cursor.rowcount)
        cursor.close()
        conn.close()
        exit()
              
else:
    print("error")
    exit()
