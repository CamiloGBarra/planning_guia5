sueldo = float(input("Ingrese el sueldo: "))
rango = int(input("Ingrese el rango (1, 2 o 3): "))

if rango == 1:
    sueldo = sueldo * 0.83
elif rango == 2:
    sueldo = sueldo * 1.2
elif rango == 3:
    sueldo = sueldo * 5
else:
    print("Rango no valido")

print("Sueldo: ", sueldo)