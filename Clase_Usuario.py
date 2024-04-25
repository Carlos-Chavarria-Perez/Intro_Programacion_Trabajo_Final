import csv
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
                if not self.__username.strip():
                    raise ValueError
                elif self.__username in Usuario.lista_usuarios:
                    raise ValueError
                else:
                    break
            except ValueError:
                print('El campo no puede estar en blanco o el usuario ya existe')
             
        self.password= input('Defina su contraseña: ')

        Persona.reistro_Integrante(self,self.username)

    
        with open("Usuarios.csv",mode="a",newline="") as archivoCSV:
            writer=csv.writer(archivoCSV,delimiter=",")
            writer.writerow([self.__username,self.__password,self.integrante])

    #Funcionliad de eliminar usuarios tanto del Archivo Usuarios como Integrantes
    def eliminar_usuario(self):
        
        with open('Usuarios.csv', mode="r") as archivoLecturaCSV:
            reader = csv.reader(archivoLecturaCSV, delimiter=",")
            next(reader)  
            for fila in reader:
                Usuario.lista_usuarios.append(fila[0])
        
        usuario_eliminar=input('Ingrese el Usuario que desea eliminar: ')
        if usuario_eliminar not in Usuario.lista_usuarios:
            print('El usuario que desea eliminar no existe en la base de datos')
            return
        lista_usuarios=[]
        lista_integrantes=[]
        
        ##Eliminacion de Archivo de Usuarios
        with open("Usuarios.csv", mode="r") as archivoCSV:
            reader = csv.reader(archivoCSV, delimiter=",")
            header=next(reader)
            for fila in reader:
                if fila[0]!= usuario_eliminar:
                    lista_usuarios.append(fila)


        with open("Usuarios.csv", mode="w", newline="") as archivoCSV:
            writer = csv.writer(archivoCSV, delimiter=",")
            writer.writerow(header)
            writer.writerows(lista_usuarios)

        ##Eliminacion de Archivo de Integrantes
        with open("Integrantes.csv", mode="r") as archivoCSV:
            reader = csv.reader(archivoCSV, delimiter=",")
            header=next(reader)
            for fila in reader:
                if fila[0]!= usuario_eliminar:
                    lista_integrantes.append(fila)


        with open("Integrantes.csv", mode="w", newline="") as archivoCSV:
            writer = csv.writer(archivoCSV, delimiter=",")
            writer.writerow(header)
            writer.writerows(lista_integrantes)

        print(f'El usuario {usuario_eliminar} ha sido removido de lista de usuarios y de integrantes')




    def actualizar_password(self,username):
        print('Para Actualizar su contraseña por favor')
        validador = input('Valide su contraseña Actual: ')
        

        with open("Usuarios.csv", mode="r") as archivoCSV:
            reader = csv.reader(archivoCSV, delimiter=",")
            header=next(reader)
            rows = list(reader)  

        for fila in rows:
            if fila[0] == username and fila[1] == validador:
                nuevo_password = input('Defina su nueva contraseña: ')
                fila[1] = nuevo_password
                print("Contraseña actualizada con éxito.")
                break
        else:
            print("Contraseña incorrecta.")
            return

    
        with open("Usuarios.csv", mode="w", newline="") as archivoCSV:
            writer = csv.writer(archivoCSV, delimiter=",")
            writer.writerow(header)
            writer.writerows(rows)

