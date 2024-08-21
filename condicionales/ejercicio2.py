#calculadora tarifa taxi

distancia = float(input("Ingrese la distancia recorrida en km/hr"))

if distancia <= 1:
    tarifa = 5
elif distancia  <= 5:
    tarifa = 5+(distancia-1)*2