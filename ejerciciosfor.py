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

def ejercicio3 ():
    año = int(input("ingrese el año: "))
    año_nacimiento = int(input("ingrese el año de nacimiento: "))
    edad = año - año_nacimiento
    print("su edad actual es: ", edad)
    for i in range(edad):
        time.sleep(2)
        print(i+1)
    return edad

#ejercicio3()

def numeros_impares():
    numero= int(input("ingrese el numero: "))

    for i in range(1, numero+1, 1):
        time.sleep(1)
        print(i)
        if i == 15:
            break;

#numeros_impares ()

def Relojero():
    segundos = int(input("ingrese los segundos a detener: "))
    for i in range(60, 1, -1):
        time.sleep(1)
        print(i)
        if i == segundos:
            print("\33[103m"+"se acabo el tiempo"+"\33[0m")
            break;
           
            

#Relojero()

def interes_anual():
    capital = float(input("ingrese el capital: "))
    tasa_interes = float(input("ingrese la tasa de interes: "))
    años = int(input("ingrese los años: "))
    for i in range(años):
        time.sleep(1)
        print(f"año {i+1}:")
        interes_anual = capital * (tasa_interes / 100)
        capital += interes_anual
        print(f"capital acumulado: ${capital:.2f}")
        print(f"interés acumulado: ${interes_anual:.2f}")
        print("----------------------------------")
        if i == años-1:
            print("\33[102m"+"se ha alcanzado el fin de los años"+"\33[0m")
            break;

#interes_anual()

def piramide():
    altura = int(input("ingrese la altura de la piramide: "))
    for i in range(1, altura + 1):
        print(" "*(altura-i), end="")
        print("*"*(2*i-1))

piramide()