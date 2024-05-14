import sys

sueldo = float(sys.argv[1])
rango = int(sys.argv[2])

if rango == 1:
    sueldo = sueldo * 0.83
elif rango == 2:
    sueldo = sueldo * 1.2
elif rango == 3:
    sueldo = sueldo * 5
else:
    print("Rango no valido")
    sys.exit(1)

print("Sueldo: ", sueldo)

"""
Ejemplos de ejecución en la terminal: hay que usar el comando "python ejercicio4.py <sueldo> <rango>"

C:\Users\camil\Downloads\MAIE\Introducción a las técnicas inteligentes de resolución de problemas 
de planificación, secuenciación y ejecución\Semana 3\Barra, Camilo - Guia 5>
python ejercicio4.py 50000 2
Sueldo:  60000.0

C:\Users\camil\Downloads\MAIE\Introducción a las técnicas inteligentes de resolución de problemas 
de planificación, secuenciación y ejecución\Semana 3\Barra, Camilo - Guia 5>
python ejercicio4.py 50000 4
Rango no valido
"""