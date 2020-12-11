from mysql import connector as conexion

usuario = 'root'
contrasena = ''
url = 'localhost'
baseDatos = 'veranos'

conn = conexion.connect(user=usuario, password=contrasena,host=url, database=baseDatos)