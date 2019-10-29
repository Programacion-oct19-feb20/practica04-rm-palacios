"""
	@author: rm-palacios
	nombre: ejercicio1.py
	descripcion: ...
"""
#System.out.printl("Ingrese su nombre")
# nombre = entrada.nextLine()

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: \n")
nota1 = input("Ingrese su nota 1: ")
nota2 = input("Ingrese su nota 2: ")

suma = nota1 + nota2


print("%s -- %s\nSu suma de nota es %s" %
	(nombre, edad, suma))



