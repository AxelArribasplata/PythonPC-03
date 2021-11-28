"""
def index (datos):

        contador = 0

        if c in datos:
            contador += 1
        return contador 
"""
"""  
class Alumno:
    def __init__(self, name,nroregistro):
        self.name = name 
        self.nroregistro = nroregistro  
        print("Se ha registrado el alumno: ", self.name)

    def __str__(self) -> str:
        return "{} ({})".format(self.name, self.nro)

    def setAge (self,edad):
        self.edad.append (edad)

datoname = input("Ingrese el nombre del alumno: ")
datoregistro = input("Ingrese el orden del alumno: ")

display = Alumno(datoname,datoregistro) 
print(f"Nombre: {display.name} || Número de registro: {display.nroregistro}") 

edad = input("Ingresar la edad del alumno: ")
print(f"Nombre: {display.name} || Número de registro: {display.nroregistro} || Edad del alumno: {edad}")   
    
"""   
   
"""
    def asignar_edad (self,edad):
        self.edad = edad
asignar = input("Asignar la edad del alumno:")

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