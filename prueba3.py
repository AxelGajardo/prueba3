import os
import globales 
import random
import math

def menu_principal():
    os.system("cls")
    print("1.- Asignar Montos Aleatorios ")
    print("2.- Estadisticas")
    print("3.- Salir")
    
    opcion = globales.seleccionar_opcion(3)

    if opcion == 1:
        print(" Asignando Montos Aleatorios ")
        crear_ventas()
    elif opcion == 2:
        print("Estadisticas")
    elif opcion == 3:
        return


def crear_ventas():
    todos_los_productos = [
        "Cafe Americano", "te chai", "Croissant", "Jugo Naranja", "Panini de Pavo y Queso", "Pastel de Zanahoria", "Espresso Doble", "Batido de Frutas", "Muffin", "Ensalada", "Chocolate Caliente",
        "Tarta de Frambuesa", "Sándwich de Huevo", "Galletas de Avena", "Frappé de Caramelo"
    ]
    ventas = globales.leer_archivo_json("productos.json")

    for i in range(15):
        precio = random.randint(20,100) * 100
        iva = precio * 0.19
        nombre = todos_los_productos

    nuevo_precio ={
        "valor":precio,
        "iva": iva,
        "nombre": todos_los_productos  
    }

    ventas.append(nuevo_precio)
    globales.guardar_archivo_json("productos.json")


menu_principal()