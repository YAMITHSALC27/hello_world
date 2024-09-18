import time

def ejercicio1 ():
    palabra =str(input("por favor ingresar palabra: "))
    cantidad = int(input("ingrese la cantidad de veces que quiere repetir la palabra: "))
    for i in range(cantidad):
        print ("valor de la variable i: ", i+1)
        time.sleep(2)
        print(palabra)
    return palabra

#ejercicio1()

def ejercicio2 ():
    edad= int(input("ingrese su edad: "))
    for i in range(edad):
        time.sleep(2)
        print(i+1)
    return edad

#ejercicio2()

