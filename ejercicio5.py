import sys
import time #esta librería se utiliza para medir el tiempo de ejecución

#Se verifica que se haya ingresado un argumento
if len(sys.argv) != 2:
    print("Uso: python ejercicio5_paralelo.py <numero>")
    sys.exit(1)

#Se verifica que el argumento sea un número entero positivo
try:
    numero = int(sys.argv[1])
    if numero <= 0:
        raise ValueError
except ValueError:
    print("El argumento debe ser un número entero positivo.")
    sys.exit(1)

#Se imprime el contador
for i in range(1, numero + 1):
    print(f"Contador {i}")
    time.sleep(1) #se detiene la ejecución del programa por 1 segundo

