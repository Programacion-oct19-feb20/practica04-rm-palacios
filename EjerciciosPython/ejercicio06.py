"""
	@author: rm-palacios
	nombre: ejercicio1.py
	descripcion: ...

	Rosa Palacios -- 23
	Su suma de notas es: 20
	Su promedio es: 10
"""
    # System.out.println("Ingrese su nombre")
	# nombre = entrada.nextLine()



nombre = input("Ingrese su nombre: \n ")
edad = input("Ingrese su edad: \n")
nota1 = input("Ingrese su nota 1: \n")
nota2 = input("Ingrese su nota 2: \n")

suma = int(nota1) + int(nota2);
promedio = (int(nota1) + int(nota2)) / 2;

print("%s -- %s\nSu suma de notas es: %s\nSu promedio es: %s" %
	(nombre, edad, suma, promedio))
