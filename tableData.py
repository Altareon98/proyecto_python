#!C:\Users\alexi\AppData\Local\Programs\Python\Python39\python.exe
import requests
import lxml.html as lh
import pandas as pd
#import cgitb
#cgitb.enable()

os.getenv('PATH_INFO')

url = 'http://localhost/p/veranos/index.html'
# Almacenar la pagina en una variable
page = requests.get(url)
# Obtener el contenido de la pagina
doc = lh.fromstring(page.content)
# Buscar y almacenar los elementos tr de la tabla
tr_elements = doc.xpath('//tr')

# Crear lista vacia
col = []
i = 0

# Por cada fila, almacenar cada primer elemento (header) y una lista vacia
for t in tr_elements[0]:
    i += 1
    name = t.text_content()
    print(i,name)
    col.append((name, []))

# Como la primera fila es el header, los datos estan guardados a partir de la segunda fila
for j in range(1, len(tr_elements)):
    # T is our j'th row
    T = tr_elements[j]
    
    # Verifica que la fila pertenezca a la tabla que buscamos 
    if len(T)!=5:
        break
    
    # i es el index de nuestra columna
    i = 0
    
    # Itera por cada elemento de la fila
    for t in T.iterchildren():
        data = t.text_content()
        # Verifica si la fila esta vacia
        if i > 0:
        # Convierte cualquier valor numerico a enteros
            try:
                data = int(data)
            except:
                pass
        # Añade datos a la lista vacia de la columna i'th
        col[i][1].append(data)
        # Incrementar i para la siguiente columna
        i += 1

col.pop(4)

Dict = {title:column for (title,column) in col}
df = pd.DataFrame(Dict)
print(df.head())

data = col