import csv
import os
import datetime
from Clase_Persona import Persona

class Usuario(Persona):
    lista_usuarios= []

    def __init__(self,username,password,integrante):
        super().__init__("","",0,integrante)
        self.__username= username
        self.__password= password

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, value):
        self.__username = value

    @password.setter
    def password(self, value):
        self.__password = value


    def registrar_usuario(self):

        with open('Usuarios.csv', mode="r") as archivoLecturaCSV:
            reader = csv.reader(archivoLecturaCSV, delimiter=",")
            next(reader)  
            for fila in reader:
                Usuario.lista_usuarios.append(fila[0])
 
        while True:
            try:
                self.__username= input('Define el usuario: ')
                if self.__username in Usuario.lista_usuarios:
                    raise ValueError
                else:
                    break
            except ValueError:
                print('Usuario ya existe')
             
        self.password= input('Defina su contraseña: ')

        Persona.reistro_Integrante(self)

    
        with open("Usuarios.csv",mode="a",newline="") as archivoCSV:
            writer=csv.writer(archivoCSV,delimiter=",")
            writer.writerow([self.__username,self.__password,self.integrante])

    def actualizar_password(self):
        validador = input('Valide su contraseña Actual: ')
        
        # Read the data from the CSV file
        with open("Usuarios.csv", mode="r") as archivoCSV:
            reader = csv.reader(archivoCSV, delimiter=",")
            rows = list(reader)  # Convert reader object to a list of rows

        # Update the specific value based on user input
        for fila in rows:
            if fila[1] == validador:
                nuevo_password = input('Defina su nueva contraseña: ')
                fila[1] = nuevo_password
                break

        # Rewrite the entire CSV file with the updated data
        with open("Usuarios.csv", mode="w", newline="") as archivoCSV:
            writer = csv.writer(archivoCSV, delimiter=",")
            writer.writerows(rows)

        if any(fila[1] == nuevo_password for fila in rows):
            print("Contraseña actualizada con éxito.")
        else:
            print("La contraseña actual no coincide con ningún usuario.")
        

class Presupuesto:
    def __init__(self,presupuesto_mensual) -> None:
        self.presupuesto_mensaul=presupuesto_mensual
        self.arhivo_presupuesto='Presupuesto.csv'
    
    def registrar_Presupuesto(self,integrante): 
        presuesto_actual=0

        if os.path.exists(self.arhivo_presupuesto):
            with open("Presupuesto.csv",mode="r",newline="") as archivoCSV:
                reader=csv.reader(archivoCSV,delimiter=",")
                for fila in reader:
                    presuesto_actual=fila[0]
                
        actualizar=input(f'Desea Actualizar el presupuesto Actual de {presuesto_actual} Si/No').upper()
        if actualizar=="SI":
            fecha=datetime.datetime.now()
            fecha_registro = fecha.strftime("%m/%Y")
            self.presupuesto_mensual=int(input('Ingrese el presupuesto del mes')) 
            with open("Presupuesto.csv",mode="a",newline="") as archivoCSV:
                writer=csv.writer(archivoCSV,delimiter=",")
                writer.writerow([self.presupuesto_mensual,fecha_registro])