import csv
import os

class Persona:
    #Roles de integrante disponibles para registrar persoma
    roles_integrantes=['Padre','Madre','Hijo','Hija']
    def __init__(self,nombre,apellido,edad,integrante) -> None:
        self.nombre=nombre
        self.apellido= apellido
        self.edad=edad
        self.integrante=integrante
        self.lista_roles_validacion=[]

    #Registro de Ingregrante
    def reistro_Integrante(self,username):
        self.username= username
        while True:
            try:
                self.nombre=input('Ingrese el nombre del integrante: ').strip().capitalize()
                if self.nombre.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                print('No puede dejar el campo en blanco solo puede ingresar letras')
        while True:
            try:
                self.apellido=input("Ingrese el apellido: ").strip().capitalize()
                if self.apellido.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                print('No puede dejar el campo en blanco solo puede ingresar letras')
        while True:
            try:
                self.edad=int(input('Ingrese la edad:'))
                if self.edad >0:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('La edad no puede ser 0 o menor a cero, tampoco puede ingresar letras o dejar el campo en blanco')
        while True:
            try:
                with open('Integrantes.csv', mode="r") as archivoLecturaCSV:
                    reader = csv.reader(archivoLecturaCSV, delimiter=",")
                    next(reader)  
                    for fila in reader:
                        self.lista_roles_validacion.append(fila[-1])

                self.integrante=input('Ingrese el rol que desea asignarle a esta persona: ').strip().capitalize()
                if self.integrante.isalpha() and self.integrante in Persona.roles_integrantes\
                      and (self.integrante !='Padre' or "Padre" not in self.lista_roles_validacion)\
                        and (self.integrante !='Madre' or "Madre" not in self.lista_roles_validacion): 
                    break
                else:
                    raise ValueError
            except ValueError:
                print('El rol que intenta no es una opcion disponible, o el role ya esta asignado')
        
        with open("Integrantes.csv",mode="a",newline="") as archivoCSV:
                writer=csv.writer(archivoCSV,delimiter=",")
                writer.writerow([self.username,self.nombre,self.apellido,self.edad,self.integrante])
                
    #Funcionaliad para poder ver todos los integrantes registrados
    def leer_Integrantes(self):
        with open("Integrantes.csv",mode="r",newline="") as archivoCSV:
            reader=csv.reader(archivoCSV,delimiter=",")
            header=next(reader)
            print("Detalles de los Integrantes:")
            for fila in reader:
                for header_item,detalle in zip(header,fila):
                    print(f'{header_item}:{detalle}')
                print()