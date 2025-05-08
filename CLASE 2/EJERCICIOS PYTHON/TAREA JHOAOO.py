#Tarea:
#Contar las vocales en una palabra ingresada por el usuario (solo a,e,i,o,u).
palabra = input("ingrese una palabra: ").lower()#.lower()=te da una copia de lo ingresado pero en MINUSCULA. como dato: .Upper() es para mayuscula
vocales = palabra.count("a") + palabra.count("e") + palabra.count("i") + palabra.count("o") + palabra.count("u")#.count nos sirve para contar un solo valor 
print(f"La palabra {palabra} tiene {vocales} vocales.")
#Imprimir la (tabla de multiplicar de un número (del 1 al 10).
numero = int(input("Ingresa un número: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
#Calcular el factorial de un número ingresado por el usuario.
numero = int(input("Ingresa un número: "))
xd = 1  
for i in range(1, numero + 1):
   xd *= i 
print(f"El factorial de {numero} es {xd}")
#Imprimir los números primos del 1 al 20.   
for num in range(1, 21):
    if num == 2 or num == 3 or num == 5 or num == 7 or num == 11 or num == 13 or num == 17 or num == 19:
        print(num)
#Sumar todos los números múltiplos de 3 o 5 menores a un número ingresado.
numero = int(input("Ingresa un número: "))
suma = 0
for i in range(1, numero):
    if i % 3 == 0 or i % 5 == 0:
        suma += i 
print(f"La suma de los múltiplos de 3 o 5 menores a {numero} es: {suma}")
#Sumar números ingresados por el usuario hasta que ingrese 0.
suma = 0
numero = int(input("Ingresa un número si deseas terminar ingresa 0: "))
while numero != 0:
    suma += numero  
    print(f"Has ingresado {numero}. La suma actual es: {suma}")
    numero = int(input("Ingresa otro número si deseas terminar ingresa 0: "))
print(f"La suma total es: {suma}")