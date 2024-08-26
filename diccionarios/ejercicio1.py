#Definir
mi_diccionario = {
    "nombre"    :   "Luis",
    "edad"      :     26,
    "ciudad"    :   "Armenia"
}

#Acceso a los valores
print(mi_diccionario["ciudad"]) #Salir: Ibague

#Añadir o actulizar
mi_diccionario["Curso"] = "Programacion POO"  #Crear
mi_diccionario["nombre"] = "David" #Actualizar

#Eliminar un elemento
#del mi_diccionario["ciudad"]
#mi_diccionario.pop("nombre")

#Iterar
for clave, valor in mi_diccionario.items():
    print(clave, valor)