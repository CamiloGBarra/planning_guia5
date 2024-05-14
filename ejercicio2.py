import os

#acá se define el directorio
directorio = 'C:\Windows\System32\drivers'

#se obtienen los elementos del directorio
elementos = os.listdir(directorio)

#se filtran los directorios
directorios = [elemento for elemento in elementos if os.path.isdir(os.path.join(directorio, elemento))]

#se imprimen los directorios
for directorio in directorios:
    print(directorio)