'''Escribir un programa que cuente cuántas vocales hay en una palabra ingresada por el usuario'''

palabra = input("Ingrese una palabra: ").lower()
vocales = "aeiou"
numeros = "1234567890"
caracteres = "!¡?()[];,.*/-+"
contador = 0
tieneNumeros = False

for letra in palabra:
    if (letra in numeros or letra in caracteres):
        tieneNumeros = True
        break

    if letra in vocales:
        contador += 1

if tieneNumeros: #Igual que: (tieneNumeros == True)
    print("Error, la palabra no es válida porque tiene números o cáracteres")
else:
    print(f"El número de vocales en la palabra {palabra} es: {contador}")