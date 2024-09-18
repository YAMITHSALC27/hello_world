def suma_dos_valores(sumando1, sumando2):
    global resultado
    resultado = sumando1 + sumando2
    return resultado

#suma_dos_valores = (4,5)
#print ("primera suma")
#print (resultado)
#suma_dos_valores = (1,2)
#print ("segunda suma")
#print (resultado)

def calculadora_dos_valores(numero1, numero2, operador):

    global resultado1
    if operador == 1:#si el operador es 1 es suma
        resultado1 = numero1 + numero2
        return resultado1
    elif operador == 2:#si el operador es 2 es resta
        resultado1 = numero1 - numero2
        return resultado1
    elif operador == 3:#si el operador es 3 es multiplicacion
        resultado1 = numero1 * numero2
        return resultado1
    elif operador == 4:#si el operador es 4 es division
        resultado1 = numero1 / numero2 
        return resultado1
    else: #si el operador es otro numero
        print("el numero ingresado no es valido")
    return resultado1

#calculadora_dos_valores(1,3,1)
#print("suma", resultado1)
#calculadora_dos_valores(4,2,2)
#print ("resta", resultado1)
#calculadora_dos_valores(1,3,3)
#print ("multiplicacion", resultado1)
#calculadora_dos_valores(2,4,4)
#print ("division", resultado1)

def calculadora_dos_valores2(numero1, numero2):
    global resultado2
    resultado2 = (numero1 * 2) + (numero2 * 2)
    return resultado2
#calculadora_dos_valores2(5,4)
#print ("respuesta", resultado2)


def pitagoras (a, b):
    global c
    c = ((a**2) + (b**2))**0.5
    return c
#pitagoras (3,4)
#print("pitagoras", c)

def despeje_x():
    global x
    #b = int(input("ingrese el valor de b= "))
    #c = int (input("ingrese el valor de c= "))
    #x= (c-b)/2
    #print ("el valor de x es: ",x)
    #return x

#despeje_x()

def logica_and():
    global x
    A= bool(input("ingrese el valor de la entrada= "))
    B= bool(input("ingrese el valor de la entrada= "))
    C= bool(input("ingrese el valor de la entrada= "))
    x= A and B and C
    print ("el valor de x es: ",x)
    return x

#logica_and()

def pitagoras_funcion_sumar():
    global resul_pitagoras
    #a=int(input("ingresar el valor de a= "))
    #b=int(input("ingresar el valor de b= "))
    #a2 = a**2
    #b2 = b**2
    #suma= suma_dos_valores(a2,b2)
    #resul_pitagoras= suma**0.5
    #print ("el valor de pitagoras es: ",resul_pitagoras)
    return resul_pitagoras

#pitagoras_funcion_sumar()

def  separador_contador():
    #global resultado_contador
    #palabra = str(input("ingrese la palabra a contar letras: "))
    #letra = str(input("ingrese la letra a contar: "))
    #resultado_contador = palabra.count(letra)
    #print ("la cantidad de letras", letra, "es= ",resultado_contador)
    #print ("la cantidad de letras de la palabra es= ", len(palabra))
    #print ("palabra separada por letras= ",list(palabra))
    #return resultado_contador

#separador_contador()

import random

# Función para determinar el ganador
def determinar_ganador(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == "piedra" and jugador2 == "tijeras") or \
         (jugador1 == "tijeras" and jugador2 == "papel") or \
         (jugador1 == "papel" and jugador2 == "piedra"):
        return "Jugador 1 gana"
    else:
        return "Jugador 2 gana"

# Función para elegir aleatoriamente piedra, papel o tijeras
def eleccion_aleatoria():
    opciones = ["piedra", "papel", "tijeras"]
    return random.choice(opciones)

# Función principal del juego
def juego():
    modo = input("¿Quieres jugar aleatoriamente? (sí/no): ")
    global eleccion_aleatoria
    
    if modo == "sí":
        jugador1 = eleccion_aleatoria()
        jugador2 = eleccion_aleatoria()
    else: 
        modo == "no"
        jugador1 = input("Jugador 1 - Elige piedra, papel o tijeras: ").lower()
        jugador2 = input("Jugador 2 - Elige piedra, papel o tijeras: ").lower()

    # Comprobar que las entradas son válidas
    opciones_validas = ["piedra", "papel", "tijeras"]

    if jugador1 not in opciones_validas or jugador2 not in opciones_validas or jugador1 and jugador2 not in opciones_validas:
        print("Una de las opciones no es válida, elige entre piedra, papel o tijeras.")
    else:
        # Mostrar el resultado
        resultado = determinar_ganador(jugador1, jugador2)
        print(f"Jugador 1 eligió: {jugador1}")
        print(f"Jugador 2 eligió: {jugador2}")
        print(f"Resultado: {resultado}")

# Ejecutar el juego
juego()
