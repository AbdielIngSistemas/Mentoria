#Hacer una calculadora que sume, reste, multiplique, divida, potencia, raiz cuadrada.
print("la calculadora funciona de la siguiente manera")
print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Potencia\n6. Raiz cuadrada\7. Salir" )
num1= int(input("Ingrese el numero de la operacion que desea realizar\n"))
if (num1==1):
    print("1. Usted eligio Sumar")
    suma=int(input("Ingrese un numero: "))
    suma2=int(input("Ingrese el numero que sumara: "))
    suma3=suma+suma2
    print("La suma es ", suma3)
elif(num1==2):
        print("2. Usted eligio Restar")
        resta=int(input("Ingrese un numero: "))
        resta2=int(input("Ingrese el numero que restara: "))
        resta3=resta-resta2
        print("la resta es",resta3)
elif(num1==3):   
            print("3. Usted eligio Multiplicar")  
            multiplicacion1=int(input("Ingrese un numero: "))
            multiplicacion2=int(input("Ingrese el numero que multiplicara: "))
            multiplicacion3=multiplicacion1*multiplicacion2   
            print(f"la multiplicacion es {multiplicacion3}")     
            #esa forma de print es mas corta xd me gusta mas         
elif(num1==4):
        print("4. Usted eligio Dividir")
        division1=int(input("Ingrese un numero: "))
        division2=int(input("Ingrese el numero que dividira: "))
        division3=division1/division2
        print(f"la division es {division3:.2f}")
elif(num1==5):
        print("5. Usted eligio Potencia")
        potencia3 = 1
        potencia1=int(input("Ingrese un numero: "))
        potencia2=int(input("Ingrese el numero de potencia: "))
        for i in range(potencia2):
               potencia3 = potencia3 * potencia1
        print("la potencia es",potencia3) #Potencia **
elif(num1==6):
        print("6. Usted eligio Raiz cuadrada")
        #el import es para crear una libreria en este caso para math el cual lo usare para que la raiz cuadrada funcione
        import math
        raiz=float(input("Ingrese un numero al cual se le sacara la raiz cuadrada"))
        raiz2=float(math.sqrt(raiz))
        print("la raiz cuadrada es",raiz2)
elif(num1==7):
    print("7. Usted eligio Salir")

