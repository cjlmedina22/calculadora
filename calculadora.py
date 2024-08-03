import math

def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: División por cero."

def exponente(x, y):
    return x ** y

def raiz_cuadrada(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."

def obtener_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

def calculadora():
    while True:
        print("\n-- Calculadora --")
        print("Selecciona la operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Exponente")
        print("6. Raíz cuadrada")
        print("7. Salir")

        seleccion = input("Ingresa tu opción (1/2/3/4/5/6/7): ")

        if seleccion == '7':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break

        if seleccion in ['1', '2', '3', '4', '5']:
            num1 = obtener_numero("Ingresa el primer número: ")
            num2 = obtener_numero("Ingresa el segundo número: ")

            if seleccion == '1':
                print(f"{num1} + {num2} = {sumar(num1, num2)}")
            elif seleccion == '2':
                print(f"{num1} - {num2} = {restar(num1, num2)}")
            elif seleccion == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif seleccion == '4':
                resultado = dividir(num1, num2)
                print(f"{num1} / {num2} = {resultado}")
            elif seleccion == '5':
                print(f"{num1} ^ {num2} = {exponente(num1, num2)}")
        elif seleccion == '6':
            num = obtener_numero("Ingresa el número para calcular la raíz cuadrada: ")
            print(f"√{num} = {raiz_cuadrada(num)}")
        else:
            print("Selección no válida. Intenta de nuevo.")

# Ejecutar la calculadora
calculadora()

#Validar entradas:

#Se agregó una función obtener_numero(mensaje)que solicita al usuario que ingrese un número y maneja el error si el usuario ingresa algo que no es un número.
#Operaciones completas:

#Se agregaron funciones para calcular exponentes ( exponente(x, y)) y raíz cuadrraiz_cuadrada(x)).
#Para calcular la raíz cuadrada, se utiliza la función math.sqrtde la libra.
#Mejorar la interfaz:

#El menú ahora incluye opciones para