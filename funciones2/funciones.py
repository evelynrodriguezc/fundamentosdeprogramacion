def funcion_externa(mensaje):
    print(f"Mensaje desde la funcion externa: {mensaje}")

    def funcion_interna():
        print(f"Mensaje desde la funcion interna {mensaje}")
        
    funcion_interna()

funcion_externa("Hola Mundo")