def calculadora(operador, x, y):
    def sumar(a, b):
        return a + b
    def restar(a, b): 
        return a - b
    def multiplicar(a, b):
        return a * b
    def dividir(a, b):
        if b != 0:
            return a / b
        else:
            return "Error, division por 0"
        
    if operador == "sumar":
        return sumar(x, y)
    elif operador == "restar":
        return restar(x, y)
    elif operador == "multiplicar":
        return multiplicar(x, y)
    elif operador == "dividir":
        return dividir(x, y)
    else: 
        return print("Error, operación no válida")
    
operador = "sumar"
x = 5
y = 3

resultado = calculadora(operador, x, y)
print(f"El resultado de {operador} {x} y {y} es = {resultado}")
        
    