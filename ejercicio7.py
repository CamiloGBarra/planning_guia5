import psutil
from datetime import datetime

# hora del sistema
hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Hora del sistema:", hora_actual)

# memoria RAM
estado_memoria = psutil.virtual_memory()
print("Memoria RAM disponible:", estado_memoria.available / (1024 ** 3), "GB") #para convertir a GB, ** es el potencia

# almacenamiento
almacenamiento = psutil.disk_usage('/')
print("Almacenamiento disponible en la partición '/':", almacenamiento.free / (1024 ** 3), "GB")
