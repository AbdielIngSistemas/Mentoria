

vocales = "aeiou"
palabra = input("ingrese una palabra: ").lower()
cont = 0
for letra in vocales:
    cont += palabra.count(letra)
print(f"La palabra {palabra} tiene {cont} vocales.")