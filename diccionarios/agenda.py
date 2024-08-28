import os 
from tabulate import tabulate

def limpiar_terminal():
    """Limpia la terminal para sistemas Unix y Win"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def mostrar_menu():
    """Muestra el menú ppal de opciones"""
    menu = (
       "\n1. Añadir contacto"
       "2. Eliminar contacto"
       "3. Buscar contacto"
       "4. Mostrar todos los contactos"
       "5. Salir"
    )
    print("\n".join(menu))
    
def gestionar_contactos(contacto, accion):
    pass