import time
import json
from procesamiento.indicadores import variables_divisas
from procesamiento.operaciones import initialize


# Abre el archivo con las credenciales para mt5
with open('otros/credenciales.txt', 'r') as file:
    content = file.read()

USER = int(content.split("USER = ")[1].split()[0].strip("'"))
PASSWORD = content.split("PASSWORD = ")[1].split()[0].strip('"')
SERVER = content.split("SERVER = ")[1].split()[0].strip('"')

# Inicia sesion en MT5
initialize(USER, PASSWORD, SERVER)


# Abre el archivo JSON para los indicadores
with open('otros/divisas.json', 'r') as archivo:
    # Carga el contenido del archivo en una lista de diccionarios
    divisas = json.load(archivo)

# Variables para los indicadores de las velas
m5  = (variables_divisas(divisas, '5m'))
m15 = (variables_divisas(divisas, '15m'))
m30 = (variables_divisas(divisas, '30m'))
h1  = (variables_divisas(divisas, '1h'))
h4  = (variables_divisas(divisas, '4h'))

vela = [m5, m15, m30, h1, h4]
print(vela)

