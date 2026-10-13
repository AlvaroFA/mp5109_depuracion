#ejemplos de tipos e variables que se van a usar

compositora = "Taylor Swift" #esto es un string
fecha_nacimiento = 1989 #esto es un entero
casada = True #esto es un booleano

paises_eras_tour = ["Estados Unidos", "Reino Unido", "Australia", "Canadá"] #esto es una lista
coordenadas = (40.7128, -74.0060) #esto es una tupla
diccionario = {"nombre": "Taylor Swift", "edad": 34, "casada": True} #esto es un diccionario
set_de_paises = {"Estados Unidos", "Reino Unido", "Australia", "Canadá"} #esto es un set

#compresion de listas

anos = [1989, 1890, 1991, 1692, 1993]
siglos  = [ (ano // 100)+1 for ano in anos] #esto es una compresion de listas que genera una nueva lista con los siglos de cada año
print(siglos) #esto imprime la lista de siglos
#[19, 18, 19, 16, 19] valores de la lista siglos

# definicion de funciones

def siglos (ano):
    return (ano // 100) + 1 #esto es una funcion que recibe un año y devuelve el siglo correspondiente

print(siglos(1989)) #esto imprime el siglo correspondiente al año 1989
# 20

