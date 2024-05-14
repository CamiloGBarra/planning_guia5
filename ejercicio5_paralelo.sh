#!/bin/bash

# $1 es el primer argumento pasado 
#al bash que será el número hasta el cual los 
#contadores deben contar.
numero=$1

if [ -z "$numero" ]; then
    echo "Uso: $0 <numero>"
    exit 1
fi

#se ejecutan 3 instancias del script en paralelo
python ejercicio5.py $numero &
pid1=$!
python ejercicio5.py $numero &
pid2=$!
python ejercicio5.py $numero &
pid3=$!

#se imprimen los pid de los procesos
echo "PID de contador1: $pid1"
echo "PID de contador2: $pid2"
echo "PID de contador3: $pid3"

#se espera a que los procesos terminen...
#wait se usa para esperar a que todos los procesos 
#secundarios finalicen antes de finalizar el script 
#de bash.
wait $pid1
wait $pid2
wait $pid3

#Para ejecutarlo:
#Desde la terminal, navegar al directorio donde se guardó 
#ejercicio5.sh y ejecutar:
# chmod +x ejercicio5.sh

# ahora se puede ejecutar el bash pasando un número hasta
# el cual los contadores deben contar. Por ejemplo, para
# contar hasta 10, se ejecuta:
# ./ejercicio5.sh 10