#Funciones

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "No se puede dividir por 0"
    return a / b

def calculadora():
    print("Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")

    opcion = input("Elija una opción (1/2/3/4): ")

    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == '1':
            print(f"Resultado: {num1} + {num2} = {suma(num1, num2)}")
        elif opcion == '2':
            print(f"Resultado: {num1} - {num2} = {resta(num1, num2)}")
        elif opcion == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicacion(num1, num2)}")
        elif opcion == '4':
            print(f"Resultado: {num1} / {num2} = {division(num1, num2)}")
    else:
        print("Operación no válida. Por favor, intente de nuevo eligiendo un número del 1 al 4.")

    otra_vez = input("Vas a hacer otra operación? (s/n): ")
    if otra_vez.lower() == "s":
        calculadora()
    else:
        print("Hasta luego")

#se ejecuta
calculadora()

