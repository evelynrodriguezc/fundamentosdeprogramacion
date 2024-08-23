calificacion = float(input("Ingrese la calificacion del estudiante: "))

if (calificacion >= 90 and calificacion <= 100): 
    print("Tienes una A")
elif calificacion >= 80 and calificacion <= 89:
    print("Tienes una B")
elif(calificacion >= 70 and calificacion <= 79):
    print("Tienes una C")
elif(calificacion >= 60 and calificacion <= 69):
    print("Tienes una D")
elif(calificacion >= 0 and calificacion <= 59): 
    print("Tienes una F")
else:
    print("Nota no valida. Debe estar entre 0 y 100")
