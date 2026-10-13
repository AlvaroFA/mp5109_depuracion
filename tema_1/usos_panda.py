import pandas as pd

#Series
capitulos = pd.Series(
[100,90,80,20],
index=["AngelesSangrientos","LobosEspaciales","AngelesOscuros","GuardiaImperial"],
name="Efectivos",
)

#recupera los efectivos de los lobos espaciales
print("Los efectivos son:",capitulos["LobosEspaciales"])
#90
#media de los efectivos
print("la media de los efectivos es ",capitulos.mean())

#medians de los efectivos
print("la mediana de los efectivos es ",capitulos.median())


#DataFrame
personajes = {
    "nombre":["logan","ragnar","dante","belial"],
    "capitulo":["lobos","lobos","sangrientos","oscuros"],
"bajas":[100,90,60,10],
}
df = pd.DataFrame(personajes)
print(df)

print("dimension del array",df.shape)
print("tipos de valores",df.dtypes)
print("dos primeros resultados",df.head(2))
print("dos ultimos resultados",df.tail(2))

print("descricion",df.describe().round(2))
print("informacion",df.info())
#filtrado de datos
print(df.loc[df["bajas"]>60, ["nombre"]])
#agrupacion de datos
print(df.groupby("capitulo")["bajas"].mean())



