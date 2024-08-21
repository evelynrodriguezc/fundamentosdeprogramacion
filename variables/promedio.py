nombre = input("Ingrese el nombre del estudiante: ")
nota1 = float(input(f"Ingrese la nota 1 {nombre}: "))
nota2 = float(input(f"Ingrese la nota 2 {nombre}: "))
nota3 = float(input(f"Ingrese la nota 3 {nombre}: "))

promedio = (nota1 + nota2 + nota3) / 3;

print(f"El promedio del estudiante de {nombre} es de {promedio}")