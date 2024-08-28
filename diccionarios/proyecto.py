def show_menu():
    print("\n1.Añadir contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Mostar todos los contactos")
    print("5. Salir")
    

def add_contact(contactos):
    nombre = input("Nombre del contacto: ")
    telefono = input("Número de teléfono: ")
    email = input("Correo electrónico: ")
    contactos[nombre] = {"telefono": telefono, "email": email}
    print(f"Contacto {nombre} añadido.")
    
def delete_contact(contactos):
    nombre = input("Nombre del contacto a eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print("Contacto no encontrado.")
        
def search_contact(contactos):
    nombre  = input("Nombre del contacto a buscar: ")
    if nombre in contactos:
        contacto = contactos[nombre]
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {contacto['telefono']}")
        print(f"Email: {contacto['email']}")
    else:
        print("Contacto no encontrado.")

def show_contacts(contactos):
    if not contactos:
        print("No hay contactos en la agenda.")
    else: 
        for nombre, info in contactos.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info['telefono']}")
            print(f"Email: {info['email']}")
            print()

def main():
    contactos = {}
    while True:
        show_menu()
        opcion = input("Selecciona una opcion: ")
        if opcion == "1":
            add_contact(contactos)
        elif opcion == "2":
            delete_contact(contactos)
        elif opcion == "3":
            search_contact(contactos)
        elif opcion == "4":
            show_contacts(contactos)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

main()