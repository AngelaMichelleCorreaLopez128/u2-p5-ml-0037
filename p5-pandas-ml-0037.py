import numpy as np
import pandas as pd
# Angela Correa NC = 0037
## datos matriz 4 x 3
datos_alumno=[
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# poner nombre a las columnas
# y almacenar la tabla en la variable df dataframe
print(" --- Datos a partir de una matrix 4 x 3 ---")
df=pd.DataFrame(datos_alumno,columns=['ci','marcas','paquete'])
print(df)
# datos a partir de un diccionario
print(" --- Datos a partir de un diccionario ---")
alumno_diccionario={
    "nombre":["Angela","Joel","Pedro","Nicole","Dylan","Catherine"],
    "califa":[100,90,90,80,70,100],
    "edad":[16,67,15,16,18,14]
}

estudiantes= pd.DataFrame(alumno_diccionario)
print(estudiantes)

print("Angela Correa NC = 0037")