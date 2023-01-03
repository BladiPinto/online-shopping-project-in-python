#Importamos los paquetes necesarios 
import pandas as pd
import numpy as np
import csv
from IPython.display import clear_output
from csv import writer


def adminLoginWindow():
    print("=====================")
    print("1.Menu")
    print("2.Agregar Producto")
    print("3.Eliminar Producto")
    print("4.Productos Disponibles")
    print("5.Cerrar sesión")
    print("=====================")


def adminDisplayMenuWindow():
    print("Id\tNombre\t\tDisponible\tPrecio\tCosto")
    print("====================================================")
    results = []
    with open('shopping.csv') as File:
        reader = csv.DictReader(File)
        for d in reader:
            print(f'{d["id"]}\t{d["nombre"]}\t\t{d["disponible"]}\t\t{d["precio"]}\t{d["costo"]}')


def addproducts():
    print("DESEA INGRESAR UN PRODUCTO :\n 1. NUEVO \n2. EXISTENTE ")
    choice = int(input("Por favor Selecciona una Opcion: "))
    if choice == 1:
        addnew()
    elif choice == 2:
        adminDisplayMenuWindow()
        addexistente()
def addnew():
    print("INGRESAR NUEVO PRODUCTO \n")
    n = int(input("Ingrese el N° de elementos nuevos : "))
    for i in range(n):
        new_id = int(input("Ingresa id : "))
        new_Nombre = input("Ingresa Nombre : ")
        new_Disponible = int(input("Cantidad : "))
        new_Precio = int(input("Ingresa Precio : "))
        new_costo = int(input("Ingresa Costo : "))
        d = [{"id": new_id, "Nombre": new_Nombre, "Disponible": new_Disponible, "Precio": new_Precio,
              "Costo": new_costo}]
        list=[new_id,new_Nombre,new_Disponible,new_Precio,new_costo]
        with open ('shopping.csv' , 'a' , newline ='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(list)
            f_object.close()
        adminDisplayMenuWindow()

def addexistente():
    new = []
    print("\n")
    dressId = input("Ingresa el ID del Producto : ")
    res=int(input("\nCuantas unidades desea aumentar ? :"))
    with open('shopping.csv') as File:
        reader = csv.DictReader(File)
        for d in reader:
            if d["id"] == dressId:
                new.append(d["id"])
                new.append(d["nombre"])
                new.append(int(d["disponible"])+res)
                new.append(d["costo"])
                new.append(d["precio"])
    with open ('shopping.csv' , 'a' , newline ='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(new)
                f_object.close()
    reemplacsv()
def removeproducts():
    new = []
    print("\n")
    dressId = input("Ingresa el ID del Producto : ")
    res=int(input("\nCuantas unidades desea eliminar ? :"))
    with open('shopping.csv') as File:
        reader = csv.DictReader(File)
        for d in reader:
            if d["id"] == dressId:
                new.append(d["id"])
                new.append(d["nombre"])
                new.append(int(d["disponible"])-res)
                new.append(d["costo"])
                new.append(d["precio"])
    with open ('shopping.csv' , 'a' , newline ='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(new)
                f_object.close()
    reemplacsv()


def reemplacsv():
    df_s =  pd.read_csv('shopping.csv')

    b=df_s.drop_duplicates(df_s.columns[~df_s.columns.isin(['nombre','disponible','precio','costo'])],keep='last')
    print(b)

    b.to_csv('shopping.csv',index=False)

def Disponibleproducts():
    Total = 0
    suma = []
    print("\n")

    print("Nombre\t\tDisponible")
    print("====================================================")

    with open('shopping.csv') as File:
        reader = csv.DictReader(File)
        for d in reader:
            print(f'{d["nombre"]}\t\t{d["disponible"]}')
            suma.append(d["disponible"])
            #Total += (d["disponible"])
    for num in map(int, suma):
        Total += num
    print("\nTotal Productos Disponibles : ", Total)


def logoutwindow():
    login()


def adminOptions():
    choice = int(input("Por favor Selecciona una Opcion: "))
    if choice == 1:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 2:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        addproducts()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 3:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        removeproducts()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 4:
        Disponibleproducts()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 5:
        logoutwindow()
    else:
        print("\nElección no válida. Por favor Ingresa elección válida")
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()


def userLoginWindow():
    print("=====================\n")
    print("1.Mostrar Menu")
    print("2.Realizar una Orden ")
    print("3.Cerrar sesiòn")
    print("\n======================")


def userDisplayMenuWindow():
    print("Id\tNombre\t\tDisponible\tPrecio")
    print("====================================================")
    results = []
    with open('shopping.csv') as File:
        reader = csv.DictReader(File)
        for d in reader:
            print(f'{d["id"]}\t{d["nombre"]}\t\t{d["disponible"]}\t\t{d["precio"]}')


def user_id():
    userDisplayMenuWindow()
    p_id = int(input("\nIngresa el id : "))


def placeOrder():
    order_number = 10
    new = []
    userDisplayMenuWindow()
    p_id = input("\nIngresa el id : ")
    res=int(input("\nCuantas unidades desea adquirir ? :"))
    with open('shopping.csv') as File:
        reader = csv.DictReader(File)
        for d in reader:
            if d["id"] == p_id:
                new.append(d["id"])
                new.append(d["nombre"])
                new.append(int(d["disponible"])-res)
                new.append(d["costo"])
                new.append(d["precio"])        
                print("\nId\tNombre\tDisponible\tPrecio")
                print("=============================================================")
                print(f'{d["id"]}\t{d["nombre"]}\t{d["disponible"]}\t\t{d["precio"]}')
                order = '{d["id"]}\t{d["nombre"]}\t{d["disponible"]}\t\t{d["precio"]}'


                conform = input("\n¿Desea realizar un pedido en el producto que se muestra arriba? Y/N ")
                
                                
                if conform == 'Y' or conform == 'y':
                    print("\nRealizó con éxito el pedido en el producto {} {}".format(d["id"], d["nombre"]))
                    order_number += 1
                    print("Su numero de orden es : ", order_number)

                    break

                elif conform == 'N' or conform == 'n':
                    print("No se realiza el pedido. Puedes continuar con tu compra. ¡¡¡¡Feliz compra!!!!")
                    break
                else:
                    print("\nHas ingresado una opción incorrecta. Por favor Ingresa de nuevo\n")
                    conform = input("\n¿Desea realizar un pedido en el producto que se muestra arriba?: Y/N ")
                    break

        if d["id"] != p_id:
            print("\nHa ingresado una identificación no válida. Por favor Ingresa identificación válida\n")
            user_id()
        print("\nProductos Disponibles : \n")

    with open ('shopping.csv' , 'a' , newline ='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(new)
        f_object.close()
    reemplacsv() 




def userChoiceOptions():
    choice = int(input("Escoge una Opcion : "))
    if choice == 1:
        userDisplayMenuWindow()
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions()
    elif choice == 2:
        placeOrder()
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions()
    elif choice == 3:
        logoutwindow()
    else:
        print("Elección no válida. Por favor Ingresa elección válida")


def login():
    tp = input("Iniciar sesión administrador/usuario de inicio de sesión \n[Escriba A para iniciar sesión en el administrador/Escriba U para iniciar sesión en el usuario] : ")
    if tp == 'A' or tp == 'a':
        password = input("Ingresa la contraseña : ")
        if password == "admin":
            adminLoginWindow()
            adminOptions()
        else:
            print("Contraseña invalida. Por favor Ingresa contraseña válida")

    elif tp == 'U' or tp == 'u':
        print("\nESCOGE UNA OPCION\n")
        option = input("1. Ingresar\n2. Registrar\n3. Quit\n Seleccion :")

        if option == "1" :
            loginUser()
        elif option == "2":
            registerUser()
        elif option == "3":
            print("¡Gracias por usar nuestro software!\n")
            login()

        elif option == "4":
            pass
        else:
            print("No has introducido una opción válida.")
        
#Resgistro de Usuarios 
def registerUser():
    with open("users.csv", mode="a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        print("\nPara registrate completa los datos y Presiona ENTER")
        print("----------------------------------------------------\n")
        email = input("E-mail: ")
        password = input("Password: ")
        password2 = input("Repetir password: ")
        clear_output()
        if password == password2:
            writer.writerow( [email, password] )
            print("\nESTAS REGISTRADO , BIENVENIDO!")
            print("******************************\n")
        else:
             print("\nAlgo salió mal. Inténtalo de nuevo.")

def loginUser():
    print("\nPara iniciar sesión, ingrese la información siguiente :")
    email = input("Email: ")
    password = input("Password: ")

    clear_output
    with open("users.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row == [email, password]:
                print("Ahora está conectado!")
                userLoginWindow()
                userChoiceOptions()
                return True
    print("Algo salió mal, intenta de nuevo.")
    return False


login()










