
import csv
import os
import datetime
import pandas as pd
import matplotlib.pyplot as plt


#separar clases por archivo
class Persona:
    roles_integrantes=['Padre','Madre','Hijo','Hija']
    def __init__(self,nombre,apellido,edad,integrante) -> None:
        self.nombre=nombre
        self.apellido= apellido
        self.edad=edad
        self.integrante=integrante
        self.lista_roles_validacion=[]

    def reistro_Integrante(self):
        while True:
            try:
                self.nombre=input('Ingrese el nombre del miemrbo: ').strip().capitalize()
                if self.nombre.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                print('No puede dejar el campo en blanco solo puede ingresar letras')
        while True:
            try:
                self.apellido=input("Ingrese el apellido del cliente: ").strip().capitalize()
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
                writer.writerow([self.nombre,self.apellido,self.edad,self.integrante])
    
    def leer_Integrantes(self):
        with open("Integrantes.csv",mode="r",newline="") as archivoCSV:
            reader=csv.reader(archivoCSV,delimiter=",")
            header=next(reader)
            print("Detalles de los Integrantes:")
            for fila in reader:
                for header_item,detalle in zip(header,fila):
                    print(f'{header_item}:{detalle}')
                print()

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


class Categoria:
    lista_categorias=[]
    def __init__(self,categoria) -> None:
        self.categoria=categoria

    @classmethod
    def leer_categorias(cls):
        cls.lista_categorias.clear()
        with open('Categorias.csv', mode="r") as archivoLecturaCSV:
            reader = csv.reader(archivoLecturaCSV, delimiter=",")
            try:
                next(reader)
            except StopIteration:
                print('El archivo esta vacio')

            for fila in reader:
                Categoria.lista_categorias.append(fila[0])

    def registrar_categoria(self):
        self.leer_categorias()
        while True:
            try:
                self.categoria=input('Ingrese la categoria que desea agregar: ').capitalize()
                if not self.categoria:
                    raise ValueError
                if self.categoria in Categoria.lista_categorias:
                    print('La categoria ya existe, no puede duplicar categorias')
                if self.categoria.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                print('No puede dejar este campo en blanco')

        with open("Categorias.csv",mode="a",newline="") as archivoCSV:
            writer=csv.writer(archivoCSV,delimiter=",")
            writer.writerow([self.categoria])

class Gastos(Categoria):
    
    def __init__(self,monto,fecha,categoria,integrante):
        super().__init__(categoria)
        self.monto=monto
        self.fecha=fecha
        self.integrante=integrante
        self.leer_categorias()

    def registro_Gasto(self,usuario_actual):

        print('Estas son las Categorias registradas actualmente')
        print(",".join(Categoria.lista_categorias))

        while True:
            try:
                self.categoria=input('Ingrese la categoria del Gasto: ').strip().capitalize()
                if self.categoria in Categoria.lista_categorias:
                    break
                else:
                    self.categoria not in Categoria.lista_categorias
                    print('La categoria seleccionada no esta registrada')
                    nuevo_registro=input('Desea registrar una nueva Categoria? Si/No: ').upper()
                    if nuevo_registro=="SI":
                        Categoria.registrar_categoria(self)
                        self.leer_categorias()
                    else:
                        break
            except ValueError:
                print('La categoria seleccionada no esta registrada')
        
        while True:
            try:
                self.monto= float(input('Ingrese el monto gastado: '))
                if self.monto >=0:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('No puede ingresar numeros negativos ni letras')

        while True:
            meses=['Ene','Feb','Mar','Abr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
            try:
                self.fecha=input('Ingrese el mes del Gasto en formato de tres letras: ').capitalize()
                largo=len(self.fecha)
                if largo !=3 or not self.fecha.isalpha() or self.fecha not in meses:
                    raise ValueError
                else:
                    break
            except ValueError:
                print('Solo puede ingresar letras y no puede dejar el campo en blanco')

        with open("Gastos.csv",mode="a",newline="") as archivoCSV:
            writer=csv.writer(archivoCSV,delimiter=",")
            writer.writerow([self.fecha,self.categoria,self.monto,self.integrante])
        
class Sistema_Presupuesto:

    def __init__(self) -> None:
        self.arhivo_presupuesto='Presupuesto.csv'
        self.archivo_integrantes='integrantes.csv'
        self.arhivo_gastos='Gastos.csv'
        self.archivo_categorias='Categorias.csv'
        self.archivo_usuarios='Usuarios.csv'
        self.usuario_actual = None

    def creacion_arvhivo_Presupuesto(self):
        if not os.path.exists(self.arhivo_presupuesto):
            with open("Presupuesto.csv",mode="w",newline="") as archivoCSV:
                writer=csv.writer(archivoCSV,delimiter=",")
                writer.writerow(['Presupuesto','Fecha de Modificacion'])
    
    def creacion_archivo_Gastos(self):
        if not os.path.exists(self.arhivo_gastos):
            with open("Gastos.csv",mode="w",newline="") as archivoCSV:
                writer=csv.writer(archivoCSV,delimiter=",")
                writer.writerow(['Fecha','Categoria','Total Gastado','Integrante'])

    def creacion_archivo_integrantes(self):
        if not os.path.exists(self.archivo_integrantes):
            with open("Integrantes.csv",mode="w",newline="") as archivoCSV:
                writer=csv.writer(archivoCSV,delimiter=",")
                writer.writerow(['Nombre','Edad','Integrante'])

    def creacion_archivo_Categorias(self):
        if not os.path.exists(self.archivo_categorias):
            with open("Categorias.csv",mode="w",newline="") as archivoCSV:
                writer=csv.writer(archivoCSV,delimiter=",")
                writer.writerow(['Categoria'])

    def creacion_archivo_Usuarios(self):
        if not os.path.exists(self.archivo_usuarios):
            with open("Usuarios.csv",mode="w",newline="") as archivoCSV:
                writer=csv.writer(archivoCSV,delimiter=",")
                writer.writerow(['Usuario','Contraseña',"Integrante"])

    def resumen_gastos(self):
        while True:
            try:
                tipo=input('Desea ver el resumen por Fecha o por Integrante?').capitalize()
                df= pd.read_csv('Gastos.csv')
                plt.style.use('ggplot')
                if tipo=="Fecha":
                    resumen= pd.DataFrame(df.groupby(['Fecha','Categoria'])['Total Gastado'].sum())
                    tabla=resumen.pivot_table(index=['Fecha'],columns='Categoria', values='Total Gastado', aggfunc='sum')
                    tabla.plot.bar(figsize=(10,10))
                    plt.title('Resumen Gastos por Fecha')
                    plt.xlabel('Fecha')
                    plt.ylabel('Total Gastado')
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.legend(title='Categoria')
                    plt.show()
                    break
                if tipo=="Integrante":
                    resumen= pd.DataFrame(df.groupby(['Integrante','Categoria'])['Total Gastado'].sum())
                    tabla=resumen.pivot_table(index=['Integrante'],columns='Categoria', values='Total Gastado', aggfunc='sum')
                    tabla.plot.bar(figsize=(10,10))
                    plt.title('Resumen Gastos por Integrante')
                    plt.xlabel('Integrante')
                    plt.ylabel('Total Gastado')
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.legend(title='Categoria')
                    plt.show()
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Esa no es una opcion valida')
    
    def restante_presupuesto(self):
        presupuesto_actual=0
        with open("Presupuesto.csv", mode="r") as archivoCSV:
            reader = csv.reader(archivoCSV, delimiter=",")
            next(reader)
            for fila in reader:
                presupuesto_actual = float(fila[0])

        df_gastos= pd.read_csv('Gastos.csv')
        total_gastado= df_gastos['Total Gastado'].sum()
        resulatdo=presupuesto_actual-total_gastado

        if resulatdo>0:
            print(f'El presuesto restante es de \033[92m{resulatdo} esta dentro del presupuesto')
        if resulatdo<0:
            print(f'El presupuesto restante es de \033[0;31m {resulatdo} esta por encima del presupuesto')
        

    print('Bienvenido a su sistema de Presupuesto Mensual')
    
    def login(self):
        while True:

            username = input("Ingrese Usuario: ")
            password = input("Ingrese Contraseña: ")
            usuario_encontrado= False

            with open("Usuarios.csv", mode="r") as archivoCSV:
                reader = csv.reader(archivoCSV, delimiter=",")
                next(reader)  
                for fila in reader:
                    if fila[0] == username and fila[1] == password:
                        integrante= fila[2]
                        self.usuario_actual=Usuario(username,password,integrante)
                        return True
                    usuario_encontrado= True

            if not usuario_encontrado:
                print('No existen usuarios actualmente, por favor registre un usuario')
                Usuario1=Usuario("","","")
                Usuario1.registrar_usuario()    
    
            print("Usuario no valido o contraseña no válida. Inténtelo de nuevo.")
            print()
    


    def ejecutar(self):
        self.creacion_arvhivo_Presupuesto()
        self.creacion_archivo_integrantes()
        self.creacion_archivo_Categorias()
        self.creacion_archivo_Usuarios()
        self.creacion_archivo_Gastos()

        if not self.login():
            return 
        
        lista_opciones=[1,2,3,4,5,6,7,8]
        
        salir="NO"
        while salir=="NO":
            print('''\033[0;37mSeleccione que desear realizar hoy
                1) Definir Presupuesto
                2) Consultar integrantes Actuales
                3) Ingresar un nuevo gasto
                4) Ingresar una nueva categoria de gasto
                5) Mostrar Graficos de gastos
                6) Consultar presupuesto restante
                7) Registrar usuario
                8) Actaulizar contaseña
                ''')

            while True:
                try:
                    opcion=int(input('Eliga un opcion: '))
                    if opcion in lista_opciones:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print('La opcion seleccionada no es valida, vuelvalo a intentar')
            
            if opcion==1:
                if self.usuario_actual.integrante not in ['Padre','Madre']:
                    print('Solo Padre o Madre pueden actualizar el presupuesto')
                else:
                    presupuesto1=Presupuesto("")
                    presupuesto1.registrar_Presupuesto(self.usuario_actual.integrante)
            if opcion==2:
                persona1=Persona("","","","")
                persona1.leer_Integrantes()
            if opcion==3:
                gasto1=Gastos("","","",self.usuario_actual.integrante)
                gasto1.registro_Gasto(self.usuario_actual.integrante)

            if opcion==4:
                categoria1=Categoria("",)
                categoria1.registrar_categoria()
            if opcion==5:
                sistemaPresupuesto.resumen_gastos()
            if opcion==6:
                sistemaPresupuesto.restante_presupuesto()
            if opcion==7:
                if self.usuario_actual.integrante not in ['Padre','Madre']:
                    print('Solo Padre o Madre pueden agregar Usuarios')
                else:
                    Usuario1=Usuario("","","")
                    Usuario1.registrar_usuario()
            if opcion==8:
                Usuario1=Usuario("","","")
                Usuario1.actualizar_password()

            salir=input('\033[0;37mDesea salir del programa de presuspuesto Si/No?: ').upper()



sistemaPresupuesto = Sistema_Presupuesto()
sistemaPresupuesto.ejecutar()
