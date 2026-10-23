import pandas as pd
import numpy as np
print("-----la tabla o DataFrame ----- NC =0124")
#Alan Romero NC 0124
n_filas= 5
n_columnas= 5
tag_colmna=tuple('ABCDE') #etiquetas para las columnas de una tupla
print(tag_colmna)
matriz=np.random.randint(1,6,size=(n_filas,n_columnas))
print("Genera matriz de 5 filas por 5 colmnas ")
print("con numeros comprendidos entre el 1 y el 10")
print(matriz)
df= pd.DataFrame(matriz,columns=tag_colmna)
print("-----la tabla o DataFrame ----- NC =0124")
print(df)
print("-----la tabla o DataFrame ----- NC =0124")
