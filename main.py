shopping = [{"id": 1001, "Nombre": "HP-AE12", "Disponible": 100, "Precio": 25000, "Costo": 24000},
            {"id": 1002, "Nombre": "DELL", "Disponible": 100, "Precio": 35000, "Costo": 34000},
            {"id": 1003, "Nombre": "ASUS", "Disponible": 100, "Precio": 28000, "Costo": 27000},
            {"id": 1004, "Nombre": "APPLE", "Disponible": 100, "Precio": 60000, "Costo": 59000},
            {"id": 1005, "Nombre": "ACER", "Disponible": 100, "Precio": 24000, "Costo": 23000},
            {"id": 1006, "Nombre": "SAMSUNG", "Disponible": 100, "Precio": 35000, "Costo": 34000},
            {"id": 1007, "Nombre": "OPPO", "Disponible": 100, "Precio": 15000, "Costo": 14000},
            {"id": 1008, "Nombre": "XAOMI", "Disponible": 100, "Precio": 45000, "Costo": 44000},
            {"id": 1009, "Nombre": "HUAWEI", "Disponible": 100, "Precio": 20000, "Costo": 19000},
            {"id": 1010, "Nombre": "VIVO", "Disponible": 100, "Precio": 12000, "Costo": 11000}]

shopping1 = shopping
temp = []
order = ""


def adminLoginWindow():
    print("=====================")
    print("1.Menu")
    print("2.Agregar Producto")
    print("3.Eliminar Producto")
    print("4.Productos Disponibles")
    print("5.Ingresos totales")
    print("6.Cerrar sesión")
    print("=====================")


def adminDisplayMenuWindow():
    print("Id\tNombre\tDisponible\tPrecio\tCosto")
    print("====================================================")
    for d in shopping:
        print(f'{d["id"]}\t{d["Nombre"]}\t{d["Disponible"]}\t\t{d["Precio"]}\t{d["Costo"]}')


def addproducts():
    n = int(input("Ingrese el N° de elementos para agregar : "))
    for i in range(n):
        new_id = int(input("Ingresa id : "))
        new_Nombre = input("Ingresa Nombre : ")
        new_Disponible = int(input("Cantidad : "))
        new_Precio = int(input("Ingresa Precio : "))
        new_costo = int(input("Ingresa Costo : "))
        d = [{"id": new_id, "Nombre": new_Nombre, "Disponible": new_Disponible, "Precio": new_Precio,
              "Costo": new_costo}]
        shopping.extend(d)
        adminDisplayMenuWindow()


def removeproducts():
    dressId = int(input("Ingresa el ID del Producto : "))
    found = False
    for d in shopping1:
        found = d["id"] == dressId
        if found != True:
            temp.append(d)
            continue
        if found == True:
            d["Disponible"] -= 1
    print("Borrando Item....")
    if len(temp) == d:
        print(f"{dressId} ")
    else:
        print(f"{dressId}'s one Disponible is removed from the list")
    adminDisplayMenuWindow()


def Disponibleproducts():
    Total = 0
    print("\n")
    for d in shopping:
        print(f'{d["Nombre"]} = {d["Disponible"]}')
        Total += (d["Disponible"])
    print("\nTotal Disponible goods is : ", Total)


def monthlyincome():
    total = 0
    for d in shopping:
        total += ((d["Disponible"] * d["Precio"]) - (d["Disponible"] * d["Costo"]))
    print("\nTotal income is : ", total)


def logoutwindow():
    login()


def adminOptions():
    choice = int(input("Please Ingresa user choice : "))
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
        monthlyincome()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 6:
        logoutwindow()
    else:
        print("\nInvalid Choice. Please Ingresa valid choice")
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()


def userLoginWindow():
    print("=====================\n")
    print("1.Display Menu")
    print("2.Place order")
    print("3.Cancel order")
    print("4.Logout")
    print("\n======================")


def userDisplayMenuWindow():
    print("Id\tNombre\tDisponible\tPrecio")
    print("===================================================")
    for d in shopping:
        print(f'{d["id"]}\t{d["Nombre"]}\t{d["Disponible"]}\t\t{d["Precio"]}')


def user_id():
    userDisplayMenuWindow()
    p_id = int(input("\nIngresa the id : "))


def placeOrder():
    order_number = 10
    userDisplayMenuWindow()
    p_id = int(input("\nIngresa the id : "))

    for d in shopping:
        if d["id"] == p_id:
            print("\nId\tNombre\tDisponible\tPrecio")
            print("=============================================================")
            print(f'{d["id"]}\t{d["Nombre"]}\t{d["Disponible"]}\t\t{d["Precio"]}')
            order = '{d["id"]}\t{d["Nombre"]}\t{d["Disponible"]}\t\t{d["Precio"]}'
            conform = input("\nDo you want to place an order on the above shown product : Y/N ")

            if conform == 'Y' or conform == 'y':
                print("\nSuccessfully placed the order on the product {} {}".format(d["id"], d["Nombre"]))
                order_number += 1
                print("Your order number is : ", order_number)
                d["Disponible"] -= 1
                break

            elif conform == 'N' or conform == 'n':
                print("The order is not placed. You can carry on with you purchase. Happy shopping!!!!")
                break
            else:
                print("\nYou have Ingresaed wrong option. Please Ingresa again\n")
                conform = input("\nDo you want to place an order on the above shown product : Y/N ")
                break

    if d["id"] != p_id:
        print("\nYou have Ingresaed invalid id. Please Ingresa valid id\n")
        user_id()
    print("\nDisponible products : \n")
    userDisplayMenuWindow()


def cancelOrder():
    found = False
    temp = []
    order_id = input("Ingresa the order id : ")
    for d in shopping:
        found = d["id"] == order_id
        if found != True:
            temp.append(d)
    if len(temp) == d:
        print(f'{order_id} is ')
    else:
        print(f'{order_id} is removed from the placed order')


def userChoiceOptions():
    choice = int(input("Please Ingresa user choice : "))
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
        cancelOrder()
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions()
    elif choice == 4:
        logoutwindow()
    else:
        print("Invalid Choice. Please Ingresa valid choice")


def login():
    tp = input("Login Admin/Login User [Type A to Login in the Admin/ Type U to Login in the User] : ")
    if tp == 'A' or tp == 'a':
        password = input("Ingresa the password : ")
        if password == "admin":
            adminLoginWindow()
            adminOptions()
        else:
            print("Invalid password. Please Ingresa valid password")

    elif tp == 'U' or tp == 'u':
        password = input("Ingresa the password : ")
        if (password == "cliente"):
            userLoginWindow()
            userChoiceOptions()
        else:
            print("Invalid password. Please Ingresa valid password")
    else:
        print("Invalid user type. Ingresa valid user type")


login()









