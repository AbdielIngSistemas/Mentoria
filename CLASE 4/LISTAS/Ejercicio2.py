#EJERCICIO 1
edad = int(input("INGRESE LA EDAD: "))
if(edad < 16):
    print("NO VOTA")
elif(16<=edad<=17 or edad>70):
    print("VOTO OPCIONAL")
elif(18<=edad<=70):
    print("OBLIGATORIO VOTAR")

#EJERCICIO 2
cantidad = int(input("INGRESE LA CANTIDAD: "))
if(5<=cantidad<=9):
    print(cantidad - (cantidad*0.05))
elif(10<=cantidad<=19):
    print(cantidad - (cantidad*0.1))
elif(cantidad>=20):
    print(cantidad - (cantidad*0.15))

#EJERCICIO 3
numero = int(input("INGRESE UN NUMERO: "))
if(numero>99 and numero<1000):
    print("TIENE 3 CIFRAS")
else:
    print("NO TIENE 3 CIFRAS")



#Ejercicio 1
edad=int(input("Ingresa tu edad: "))
 
if edad<16:
    print("Usted no puede votar")
elif 16<=edad<=18 or edad>70:
    print("Su voto es opcional")
elif 18<=edad<=70:
    print("Su voto es obligatorio")
#Ejercicio 2
cantidad=int(input("Ingresa la cantidad de productos comprados: "))
 
if 5<=cantidad<= 9:
    descuento=5
elif 10<=cantidad<=19:
    descuento=10
elif cantidad>=20:
    descuento=15
else:
    descuento=0
 
print("Descuento del: ", descuento,"%")
#Ejercicio 3
numero=int(input("Ingresa un número: "))
 
if 100<=abs(numero)<=999:
    print("El número tiene 3 cifras.")
else:
    print("El número NO tiene 3 cifras.")