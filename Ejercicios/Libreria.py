#Vamos a crear un programa que utilice un diccionario para gestionar información sobre libros en una biblioteca. Cada libro estará representado por su título como clave y el número de ejemplares disponibles como valor.

#1. Define un diccionario llamado **`biblioteca`** con al menos cinco libros y la cantidad de ejemplares disponibles para cada uno.

biblioteca = {
    "48 leyes de poder": 2,
    "Padre rico, padre pobre": 5,
    "Séneca": 35,
    "Cartas de Lucilio": 11,
    "La llamada del coraje": 2,
}

#2. Implementa una función llamada `prestar_libro` que acepte el título de un libro y la cantidad de ejemplares que se van a prestar. La función deberá restar la cantidad prestada del total de ejemplares disponibles. Asegúrate de manejar casos en los que la cantidad prestada sea mayor que la cantidad disponible.

def prestar_libro(titulo_libro, cantidad_prestar):
    if titulo_libro in biblioteca:
        if cantidad_prestar <= biblioteca[titulo_libro]:
            biblioteca[titulo_libro] -= cantidad_prestar
            print(f"Has prestado {cantidad_prestar} ejemplares del libro {titulo_libro}.\nAún quedan {biblioteca[titulo_libro]} Uds Disponibles")
        else:
            print(f"No hay suficientes ejemplares del libro {titulo_libro} para prestar {cantidad_prestar}. Solo hay {biblioteca[titulo_libro]} disponibles.")
    else:
            print(f"El libro {titulo_libro} no existe.") 


insercion = input("Inserte su libro que desea prestar:\n")
titulo_libro = insercion.title()
cantidad_prestar = int(input(f"¿Cuántos ejemplares del libro {titulo_libro} desea prestar?\n"))
prestar_uno = prestar_libro(titulo_libro, cantidad_prestar)

#3. Implementa una función llamada **`devolver_libro`** que acepte el título de un libro y la cantidad de ejemplares que se van a devolver. La función deberá sumar la cantidad devuelta al total de ejemplares disponibles. Asegúrate de manejar casos en los que la cantidad devuelta sea mayor que la cantidad prestada.

def devolver_ejemplares_libro(titulo_libro, cantidad_libro):
    if titulo_libro in biblioteca:
        if cantidad_libro <= biblioteca[titulo_libro]:
            biblioteca[titulo_libro] += cantidad_libro
            print(f"Se han añadido {cantidad_libro} ejemplares del libro {titulo_libro} a la biblioteca.\nEl total de ejemplares disponibles es de {biblioteca[titulo_libro]}.")
        else:
            print(f"La cantidad actual del libro {titulo_libro} es de {biblioteca[titulo_libro]} Uds")
    else:
        biblioteca[titulo_libro] = cantidad_libro
        print(f"Se ha registrado el libro {titulo_libro} con {cantidad_libro} ejemplares.")


insercion2 = input("Inserte el nombre del libro que recibe:\n")
libro_insertado = insercion2.title()

print(f"¿Cuantas unidades de {libro_insertado} recibe?:\n")
cantidad_uds = int(input())
libro_new = devolver_ejemplares_libro(libro_insertado, cantidad_uds)

#4. Implementa una función llamada **`ver_inventario`** que imprima todos los libros en la biblioteca y la cantidad de ejemplares disponibles.

def ver_inventario():
     print("El inventario actual:\n")
     libros_con_unidades = []
     for libros, unidades in biblioteca.items():
         libros_con_unidades.append((libros, unidades))
     return libros_con_unidades

print(ver_inventario())
    
#5. Utiliza las funciones para realizar operaciones de préstamo, devolución e imprimir el inventario.

def seleccionar_operacion():
    print("\n¿Qué operación desea realizar?\n\n1. Prestar libro\n2. Devolver libro\n3. Ver inventario")
    operacion = int(input())
    return operacion


operacion = seleccionar_operacion()

if operacion == 1:
    titulo_libro = input("Inserte el título del libro que desea prestar:\n")
    cantidad_prestar = int(input(f"¿Cuántos ejemplares del libro {titulo_libro} desea prestar?\n"))
    prestar_libro(titulo_libro, cantidad_prestar)

elif operacion == 2:
    titulo_libro = input("Inserte el título del libro que desea devolver:\n")
    cantidad_devolver = int(input(f"¿Cuántos ejemplares del libro {titulo_libro} desea devolver?\n"))
    devolver_ejemplares_libro(titulo_libro, cantidad_devolver)

else:
    print(ver_inventario())