while(True):
    print ("elija una opcion ")

    print ("a) SUMA")
    print ("b) RESTAR")
    print ("c) MULTIPLICAR")
    print ("d) DIVIDIR")
    print ("e) ELEVAR")
    print ("f) salir")




    opc = input()

    if (opc == "a"):
        a=float(input("ingrese numero1:"))
        b=float(input("ingrese numero2:"))
        resultado = a+b
        print("el resultado es",resultado)
    if (opc == "b"):
        a = float(input("ingrese numero1:"))
        b = float(input("ingrese numero2:"))
        resultado = a-b
        print("el resultado es", resultado)
    if (opc == "c"):
        a = float(input("ingrese numero1:"))
        b = float(input("ingrese numero2:"))
        resultado = a*b
        print("el resultado es", resultado)
    if (opc == "d"):
        a = float(input("ingrese numero1:"))
        b = float(input("ingrese numero2:"))
        resultado = a / b
        print("el resultado es", resultado)

    if (opc == "e"):
        a = float(input("ingrese numero1:"))
        b = float(input("ingrese numero2:"))
        resultado = a**b
        print("el resultado es", resultado)

    if (opc == "f"):
        exit()

