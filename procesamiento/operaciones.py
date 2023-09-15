import MetaTrader5 as mt5
import datetime
# import pickle
import time
import os


# Inicialización de MetaTrader5
def initialize(login, password, server):
    mt5.initialize()

    if not mt5.initialize():
        print("Error al conectarse a MetaTrader5")
        mt5.shutdown()
        quit()

    authorized = mt5.login(login, password, server)
    if not authorized:
        print("Failed to connect at account #{}. Error code: {}".format(PASSWORD, mt5.last_error()))

    print('Login exitoso')


# Ciclo de operaciones dependiendo
def operaciones():
    pass