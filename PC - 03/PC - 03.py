#EJERCICIO 01 

#FORMA 01
"""
 def longitud(cadena):
    
    contador = 0
    
    for c in cadena:
        contador += 1
    return contador

my_string = input("Ingresar el texto: ")
lista_palabras = my_string.split()

print('\033[1m',"El texto ingresado es: {}".format(my_string),'\033[0m')
print('\033[1m',f"La ultima palabra es {lista_palabras[-1]} y su longitud es de {longitud(lista_palabras[-1])} caracteres.",'\033[0m')

"""


#FORMA 02 (Importando otro archivo)
"""
import Operaciones

my_string = input("Ingresar el texto: ")
lista_palabras = my_string.split()

print("El texto ingresado es: {}".format(my_string))
print(f"La ultima palabra es {lista_palabras[-1]} y su longitud es de {Operaciones.longitud(lista_palabras[-1])} caracteres.")

"""

#EJERCICIO 02

"""
def mayuscula_primer_caracter(frase):
    resultado=""
    for p in frase.split():
        resultado += p[0].upper() + p[1::] + " "
    return resultado
texto= input("Ingrese el texto: ")
print(mayuscula_primer_caracter(texto))

"""

#EJERCICIO 03 
"""
class circulo:
    def _init_(self, radio, pi):
        self.radio = radio
        self.pi = pi

pi=3.1416
radio=float(input("Ingrese el area: "))
area=pi*radio**2
print("El area del circulo es: ", area)

"""

#EJERCICIO 04

"""
class rectangulo:
    def _init_(self, base, altura):
        self.base = base
        self.altura = altura
base=float(input("Ingrese la base: "))
altura=float(input("Ingrese la altura: "))
area= base * altura
print("El area del rectangulo es: ", area)
"""

#EJERCICIO 05
"""
class Alumno:
    def __init__(self, name,nroregistro,edad,nota):
        self.name = name 
        self.nroregistro = nroregistro 
        self.edad = edad
        self.nota = nota 
        print('\033[1m',"Se ha registrado el alumno: ", self.name,'\033[0m')

    def __str__(self) -> str:
        return "{} ({})".format(self.name, self.nroregistro)
    
    def display (self):
        print(f"Nombre: {self.name}")
        print(f"Número de registro: {self.nroregistro}")

    def setAge (self,edad):
        self.edad.append (edad)
    
    def setNota (self,nota):
        self.nota.append (nota)
 
cust1 = Alumno('Axel','01','23 años','16 puntos')

print(f"El nombre del alumno es: {cust1.name}")
print(f"El numero de registro es: {cust1.nroregistro}")
print("La edad del alumno es: {}".format(cust1.edad))
print("La nota del alumnos es: {}".format(cust1.nota))

cust2 = Alumno('Carlos','02','28 años','19 puntos')

print(f"El nombre del alumno es: {cust2.name}")
print(f"El numero de registro es: {cust2.nroregistro}")
print("La edad del alumno es: {}".format(cust2.edad))
print("La nora del alumnos es: {}".format(cust2.nota))  
"""

#Se puede realizar tambien con entrada de valores osea con un input.


#EJERCICIO 06

"""
print ('\033[1m',"¡BIENVENIDO!, ingrese las calificaciones",'\033[0m')
Lista = []
    
try:
    n = 3
    for i in range(n): 
        new_element = float(input("Ingrese nota: ")) 
        Lista.append(new_element)
    print('\033[1m',f"Las calificaciones son: {Lista}",'\033[0m')
    
    Lista_entero = [ round(x) for x in Lista]

    print(f"La primera calificación individual de valor entero es: {Lista_entero[0]}") 
    print(f"La segunda calificación individual de valor entero es: {Lista_entero[1]}")  
    print(f"La tercera calificación individual de valor entero es: {Lista_entero[2]}")

except:
    print("¡Ha ocurrido un error!, los valores no pueden ser convertidos debido a un error de formato")
"""

#EJERCICIO 07
"""
n = int(input("Ingrese el numero de filas: "))
def triangulo_pascal(filas):
	fila=[1]
	cero=[0]
	for i in range(filas):
		print(fila)
		fila=[i + d for i, d in zip(fila + cero, cero + fila)]
triangulo_pascal(n)
"""
#EJERCICIO 08





#EJERCICIO 09
"""
import random

numero=random.randint(1,100)
intentos=0
jugando=True
print("===ADIVINA UN NUMERO DEL 1 AL 100===")
while jugando:
	intentos += 1
	if intentos <= 7:
		eleccion=int(input("Dime un numero del 1 al 100: "))
		if eleccion==numero:
			print("Has acertado.Has necesitado", intentos, "intentos.")
			jugando=False
		elif eleccion > numero:
			print("Demasiado alto.Llevas" , intentos, "intentos.")
		elif eleccion < numero:
			print("Demasiado bajo.Llevas" , intentos, "intentos.")
	else:
		print("Se te acabaron los intentos. Has perdido.")
		jugando=False

"""

#EJERCICIO 10
"""
import Operaciones
import math
print("Bienvenido al menú interactivo")

while True:

    print("""¿Qué quieres hacer? Escribe una opción
    1) Sumar dos números
    2) Restar dos números
    3) Producto de dos números
    4) División de dos números
    5) Salir""")
    
    opcion=int(input())
    if opcion == 1:
        a=float(input("Introduce un numero: "))
        b=float(input("Introduce un numero: "))

        resultado=Operaciones.suma(a, b)
        print(resultado)

    elif opcion == 2:
        a=float(input("Introduce un numero: "))
        b=float(input("Introduce un numero: "))

        resultado=Operaciones.resta(a, b)
        print(resultado)

    elif opcion == 3:
        a=float(input("Introduce un numero: "))
        b=float(input("Introduce un numero: "))

        resultado=Operaciones.producto(a, b)
        print(resultado)

    elif opcion == 4:
        a=float(input("Introduce un numero: "))
        b=float(input("Introduce un numero: "))

        resultado=Operaciones.division(a, b)
        print(resultado)

    elif opcion == 5:
        print("Gracias por usar el menú interactivo")
        break
    else:
        print("Comando desconocido. Ingresa una opcion valida.")

"""