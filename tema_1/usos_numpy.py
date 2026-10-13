import numpy as np

numeros= np.array([11,20, 15, 18, 22])
elementos = numeros.shape
tipo = numeros.dtype
dimensiones = numeros.ndim

print("el numero de elementos es ",elementos)
print("el tipo de datos es ",tipo)
print("el numero de dimensiones es ",dimensiones)

#uso de array multidimensional
multidimensional  = np.array([[1,2,3],[4,5,6]])
print(multidimensional[1,1]) # devuelve el numero 5

#vectorizacion de valores

edades= np.array([1,2,3,4,5,6,7,8])
valorMinimo = edades.min()
valorMaximo= edades.max()
media =  edades.mean()
mediana= np.median(edades)

print("la media es ", media)
print ("la mediana es ", mediana)
print ("el valor minimo es ", valorMinimo)
print ("el valor maximo es ", valorMaximo)

particiones = (media / edades)
print("resultado sin acotar decimales",particiones)
res_particiones=np.round(particiones,3)
print("Acotando a 3 deciama;es",res_particiones)
#desviacion tipica poblacional
desviacionTipica = edades.std()
print ("desviacion tipica", desviacionTipica)
# desviacion tipica muestral
desviacionMuestral =edades.std(ddof=1)
print ("desviacion muetral", desviacionMuestral)
#indices booleanos
valores= np.array([1,2,3,4,5,6,7])
booleano = valores[valores < 5]
print("valores menores de 5", booleano)
