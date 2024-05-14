#!/bin/bash

# Obtener el argumento
numero=$1

# Verificar si se pasó un argumento
if [ -z "$numero" ]; then
    echo "Uso: $0 <numero>"
    exit 1
fi

# Ejecutar el script de Python tres veces de manera secuencial
python ejercicio5.py $numero &
pid1=$!
echo "PID de contador1: $pid1"
wait $pid1

python ejercicio5.py $numero &
pid2=$!
echo "PID de contador2: $pid2"
wait $pid2

python ejercicio5.py $numero &
pid3=$!
echo "PID de contador3: $pid3"
wait $pid3

#Para ejecutarlo:
#Desde la terminal, navegar al directorio donde se guardó 
#ejercicio5.sh y ejecutar:
# chmod +x ejercicio5.sh

# ahora se puede ejecutar el bash pasando un número hasta
# el cual los contadores deben contar. Por ejemplo, para
# contar hasta 10, se ejecuta:
# ./ejercicio5.sh 10