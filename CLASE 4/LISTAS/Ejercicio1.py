#Crea una lista llamada numeros con estos 5 números: 10, 20, 30, 40, 50.
#Imprime el primer número de la lista.
#Imprime el último número de la lista.
#Suma el segundo y el tercer número, e imprime el resultado.

import funciones
numeros = [10, 20, 30, 40, 50]
print(numeros[0])
print(numeros[4])
print(funciones.suma(numeros[1],numeros[2]))
cont = 0
for n in numeros:
    cont = funciones.suma(cont, n)

print(cont)
 