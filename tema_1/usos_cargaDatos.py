import os

import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "a.csv"))

datos = pd.DataFrame(df)
#saber tipos de los datos del csv
print(datos.dtypes)
#filtrado de datos
print(datos.loc[(datos["Idade"] <25) & (datos["Defensa"] >9 ) , ["Nome","Salario","Idade"]])
#metiendo los datos en una variable
filtrado = datos.loc[(datos["Idade"] <25) & (datos["Defensa"] >9 ) , ["Nome","Salario","Idade","Defensa"]]
print("Datos",filtrado)
print("Media de defensa por idade",datos.groupby("Idade")["Defensa"].mean().round(2))
print(datos.loc[(datos["Idade"] <25) & (datos["Defensa"] >9 ) , ["Nome","Salario","Idade","Defensa"]].groupby("Idade")["Defensa"].mean().round(2))
print("con variable filtrado",filtrado.groupby("Idade")["Defensa"].head(3).index)
jugadores= filtrado.groupby("Idade")["Defensa"].head(3).index
#obteniendo los datos de los indices de la consulta anterior
print("Mostrando nombre de los jugadores que tienen menos de 25 y defensa mayor que 9:",filtrado.loc[jugadores,["Nome"]])



#leyendo un json
df = pd.read_json(os.path.join(os.path.dirname(os.path.abspath(__file__)), "TS.json"),orient='records')

datos = pd.DataFrame(df)
print(pd.DataFrame(df).dtypes)
print("Numero de canciones",datos["albums"][1]["tracks"])
print("Nombre del primer album",datos["albums"][0]["title"])

df_albums = pd.DataFrame(datos["albums"])
print("albums de TS:",df_albums)
