import csv
import os
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from Clase_Persona import Persona
from Clase_Usuario import Usuario
from Clase_Presupuesto import Presupuesto
from Clase_Categorias import Categoria
from Clase_Gastos import Gastos





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
                writer.writerow(['Usuario','Nombre','Apellido','Edad','Integrante'])

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
        
        lista_opciones=[1,2,3,4,5,6,7,8,9]
        
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
                9) Eliminar Usuario
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
                Sistema_Presupuesto.resumen_gastos(self)
            if opcion==6:
                Sistema_Presupuesto.restante_presupuesto(self)
            if opcion==7:
                if self.usuario_actual.integrante not in ['Padre','Madre']:
                    print('Solo Padre o Madre pueden agregar Usuarios')
                else:
                    Usuario1=Usuario("","","")
                    Usuario1.registrar_usuario()
            if opcion==8:
                Usuario1=Usuario("","","")
                Usuario1.actualizar_password()
            if opcion==9:
                if self.usuario_actual.integrante not in ['Padre','Madre']:
                    print('Solo Padre o Madre pueden eliminar Usuarios')
                else:
                    Usuario1=Usuario("","","")
                    Usuario1.eliminar_usuario()
            while True:
                try:
                    salir=input('\033[0;37mDesea salir del programa de presuspuesto Si/No?: ').upper()
                    if salir.upper()=="SI" or salir.upper()=="NO":
                        break
                    else:
                        raise ValueError
                except:
                    ValueError
                    print('Esa no es una opcion valida')


