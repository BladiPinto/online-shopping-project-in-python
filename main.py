#Importamos los paquetes necesarios 
import pandas as pd
import csv 
from IPython.display import clear_output
from csv import writer

#Funcion para mostrar el menu del administrador
def adminLoginWindow():
    print("=====================")
    print("1.Menu")
    print("2.Agregar Producto")
    print("3.Eliminar Producto")
    print("4.Productos Disponibles")
    print("5.Cerrar sesión")
    print("=====================")

#Funcion para mostrar ventana de productos
def VentanaProductos():
    print("Id\tNombre\t\tDisponible\tPrecio\tCosto")
    print("====================================================")
    results = []
    with open('shopping.csv') as File:
        reader = csv.DictReader(File)
        for d in reader:
            print(f'{d["id"]}\t{d["nombre"]}\t\t{d["disponible"]}\t\t{d["precio"]}\t{d["costo"]}')

#Funcion para agregar Productos
def addproducts():
    print("DESEA INGRESAR UN PRODUCTO :\n1. NUEVO \n2. EXISTENTE ")
    choice = int(input("Por favor Selecciona una Opcion: "))
    if choice == 1:
        addnew()
    elif choice == 2:
        addexistente()

#Agregar un producto NUEVO 
def addnew():
    print("INGRESAR NUEVO PRODUCTO \n")
    n = int(input("Ingrese el N° de elementos nuevos : "))
    for i in range(n):
        new_id = int(input("Ingresa id : ")) # 3131
        new_Nombre = input("Ingresa Nombre : ") # nombre
        new_Disponible = int(input("Cantidad : ")) # 100
        new_Precio = int(input("Ingresa Precio : ")) # 150
        new_costo = int(input("Ingresa Costo : ")) # 120

        #array list [3131, nombre , 100 , 150 , 120]
        list=[new_id,new_Nombre,new_Disponible,new_Precio,new_costo]

        #Escribir nueva linea en el CSV
        with open ('shopping.csv' , 'a' , newline ='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(list)
            f_object.close()

        #Mostrar los productos
        VentanaProductos()

#Agregar Existente
def addexistente():
    new = []
    print("\n")
    dressId = input("Ingresa el ID del Producto : ") # 1001
    aumentar=int(input("\nCuantas unidades desea aumentar ? :")) # 100
    with open('shopping.csv') as File:
        reader = csv.DictReader(File)
        for d in reader:
            if d["id"] == dressId: # Comparación con el ID existente
                new.append(d["id"]) # new [ 1001 ]
                new.append(d["nombre"]) # new [ 1001 , HPAE12 ]
                new.append(int(d["disponible"])+aumentar) #new [1001 , HPAE12, 200 ]
                new.append(d["costo"])  # new[1001 , HPAE12 , 200 , 25000]
                new.append(d["precio"]) # new[1001, HPAE12,200 , 25000 ,24000]

    #Guardar en el CSV como nueva linea      
    with open ('shopping.csv' , 'a' , newline ='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(new)
                f_object.close()

    #Funcion para reemplazar en el csv
    reemplacsv()

#Funcion para eliminar o remover Productos
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
                #Restar a los productos disponibles
                new.append(int(d["disponible"])-res)
                new.append(d["costo"])
                new.append(d["precio"])
    
    #Escribir en el csv como una nueva linea
    with open ('shopping.csv' , 'a' , newline ='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(new)
                f_object.close()
    #Eliminar duplicados
    reemplacsv()

# Reemplazar duplicados 
def reemplacsv():
    df_s =  pd.read_csv('shopping.csv')

    #Eliminar el duplicado y consevar el ULTIMO elemento de acuerdo al ID 
    b=df_s.drop_duplicates(df_s.columns[~df_s.columns.isin(['nombre','disponible','precio','costo'])],keep='last')
    print(b)

    #Convertir en CSV  
    b.to_csv('shopping.csv',index=False)

#funcion de Productos disponibles
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
            #append para agregar al Array suma el valor de disponible
            suma.append(d["disponible"])

    #Buble para sumar  y convertir el Valor caracter a Entero
    for num in map(int, suma):
        Total += num
    print("\nSuma total Productos Disponibles : ", Total)

#Para salir al inicio  
def logoutwindow():
    login()

#Funcion para controlar el menu del administrador
def adminOptions():
    choice = int(input("Por favor Selecciona una Opcion: "))
    if choice == 1:
        VentanaProductos()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 2:
        VentanaProductos()
        print("\n===================================================\n")
        addproducts()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 3:
        VentanaProductos()
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


############# MODO USUARIO #################

#Menu del Usuario
def userLoginWindow():
    print("=====================\n")
    print("1.Mostrar Menu")
    print("2.Realizar una Orden ")
    print("3.Cerrar sesiòn")
    print("\n======================")


# Mostras los productos
def userDisplayMenuWindow():
    print("Id\tNombre\t\tDisponible\tPrecio")
    print("====================================================")
    
    #Leer fila por fila el csv e imprimir
    with open('shopping.csv') as File:
        reader = csv.DictReader(File)
        #imprimiendo
        for d in reader:
            print(f'{d["id"]}\t{d["nombre"]}\t\t{d["disponible"]}\t\t{d["precio"]}')

#Funcion Error de ID
def user_id():
    userDisplayMenuWindow()
    p_id = int(input("\nIngresa el id : "))

#Realizar una compra
def placeOrder():
    order_number = 10
    new = []
    #Mostrar los productos
    userDisplayMenuWindow()

    p_id = input("\nIngresa el id : ")

    adquirir=int(input("\nCuantas unidades desea adquirir ? :")) # 50

    #Realizar la operacion de compra
    with open('shopping.csv') as File:
        reader = csv.DictReader(File)
        for d in reader:
            #Comparando el ID
            if d["id"] == p_id:
                new.append(d["id"])
                new.append(d["nombre"])
                new.append(int(d["disponible"])-adquirir) #  100 - 50
                new.append(d["costo"])
                new.append(d["precio"])        
                print("\nId\tNombre\tDisponible\tPrecio")
                print("=============================================================")
                print(f'{d["id"]}\t{d["nombre"]}\t{d["disponible"]}\t\t{d["precio"]}')
                order = '{d["id"]}\t{d["nombre"]}\t{d["disponible"]}\t\t{d["precio"]}'


                conform = input("\n¿Desea realizar un pedido en el producto que se muestra arriba? Y(yes)/N(no) = ")
                
                                
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

    #Guardar como nueva linea en el csv
    with open ('shopping.csv' , 'a' , newline ='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(new)
        f_object.close()

    #Eliminar duplicados
    reemplacsv() 



#Funcion para controlar el menu del usuario
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


#Seleccion del modo a utilizar el Prototipo
def login():
    tp = input("Iniciar sesión administrador/usuario de inicio de sesión \n[Escriba A para iniciar sesión en el administrador/Escriba U para iniciar sesión en el usuario] : ")
    #controlar la opcion del tp A 0 ADMINISTRADOR y U=USUARIO
    if tp == 'A' or tp == 'a':
        password = input("Ingresa la contraseña : ")

        if password == "admin":
            #si la contraseña es correcta te muestra el menu y las opciones
            adminLoginWindow()
            adminOptions()
        else:
            print("Contraseña invalida. Por favor Ingresa contraseña válida")
    #usuario
    elif tp == 'U' or tp == 'u':
        print("\nESCOGE UNA OPCION\n")
        option = input("1. Ingresar\n2. Registrar\n3. Salir\nSelecciona una Opcion :")

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
        
#Funcion de Registro de Usuarios 
def registerUser():
    #Escribir una nueva linea en el Csv users.csv
    with open("users.csv", mode="a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        print("\nPara registrate completa los datos y Presiona ENTER")
        print("----------------------------------------------------\n")
        email = input("E-mail: ")
        password = input("Password: ")
        password2 = input("Repetir password: ")

        clear_output()
        #Verificando Contraseñas
        if password == password2:
            #Escribir nueva linea
            writer.writerow( [email, password] )
            print("\nESTAS REGISTRADO , BIENVENIDO!")
            print("******************************\n")
        else:
             print("\nAlgo salió mal. Inténtalo de nuevo.")

# Funcion de Ingresar Usuario
def loginUser():
    print("\nPara iniciar sesión, ingrese la información siguiente :")
    #Guardando datos del usuario
    email = input("Email: ")
    password = input("Password: ")

    clear_output
    #abrir el csv en moda Lectura "Read"
    with open("users.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            #Validando datos
            if row == [email, password]:
                print("\nAhora está conectado!\n")
                #Mostrando el menu del usuario
                userLoginWindow()
                userChoiceOptions()
                return True

    print("Algo salió mal, intenta de nuevo.")
    return False


login()










