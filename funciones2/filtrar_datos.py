
def procesar_nums(numeros:list):
    def es_positivo(n):
        return n > 0
    
    def es_negativo(n):
        return n < 0
    
    def es_par(n):
        return n % 2 == 0
    
    def filtro(lista):
        total_positivos  = 0
        total_negativos = 0
        total_pares = 0
        
        for numero in lista:
            if es_positivo(numero):
                total_positivos += numero
            if es_negativo(numero):
                total_negativos += numero
            if es_par(numero):
                total_pares += numero 
        return[total_positivos, total_negativos, total_pares]
    return filtro(numeros)

numeros = [-5, 5, 2, 15, 9, -4]

resultados = procesar_nums(numeros)

'''
Ejemplos para imprimir como Diccionario
print(f"Suma de números positivos: {resultados["Positivos"]}")
print(f"Suma de números negativos: {resultados["Negativos"]}")
'''

print(f"La suma de números positivos es: {resultados[0]}")
print(f"La suma de números negativos es: {resultados[1]}")
print(f"La suma de números pares es: {resultados[2]}")

