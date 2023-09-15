import MetaTrader5 as mt5
import datetime
# import pickle
import time
import os

from procesamiento.indicadores import variables_divisas


# Leer las credenciales desde el archivo 'credenciales_mt.txt'
with open('otros/credenciales.txt', 'r') as file:
    content = file.read()

USER = int(content.split("USER = ")[1].split()[0].strip("'"))
PASSWORD = content.split("PASSWORD = ")[1].split()[0].strip('"')
SERVER = content.split("SERVER = ")[1].split()[0].strip('"')

# print(USER)
# print(PASSWORD)
# print(SERVER)

# retirar
divisas = [{"symbol": "BTCUSD", "screener": "crypto", "exchange": "EXMO" },
            {"symbol": "EURUSD", "screener": "forex", "exchange": "FX_IDC"}]


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


initialize(USER, PASSWORD, SERVER)


# checamos el balance
account_info_dict = mt5.account_info()._asdict()
balance = account_info_dict['balance']

# para el valor del lotaje
# lot = round(((balance/1000) * 0.3), 2)
print(account_info_dict)

m5 = (variables_divisas(divisas, '5m'))
# print(m5)


def operaciones(vela):
    print(vela)
    for i in range(len(vela)):
        symbol = vela[i]['symbol']
        tipo = vela[i]['tipo']
        precio = vela[i]['precio']
        interval = vela[i]['interval']
        sl = vela[i]['sl']
        tp = vela[i]['tp']
        lot = round(((balance/1000) * 0.3), 2)
        comentario = symbol + ' ' + tipo + ' ' + interval

        # Agregar condicional:
        # Si comentario ya existe en operaciones de mt5, ignore
        # Revisar operaciones activas en mt5 

    
    # time.sleep(20)


    pass

operaciones(m5)












# print('')
# print(f'balance: {balance}')
# print(f'lotaje: {lot}')
# print(account_info_dict)


#     # Preparar la solicitud de compra
#     symbol = dict_1['symbol']
    
#     # reemplaza la T en BTCUSDT/TUSDBTC o cualquier otra crypto
#     if "USDT" in symbol:
#         symbol = symbol[:-1]
#     elif "TUSD" in symbol:
#         symbol = symbol[1:]
    
#     # para comentario en mt5
#     comentario = dict_1['comment'] + ' ' + dict_1['period']

#     # lot = 0.1
#     # point = mt5.symbol_info(symbol).point # presenta error en algunas monedas (no se usa)
#     price = float(dict_1['price'])
#     sl = float(dict_1['sl'])
#     tp = float(dict_1['tp'])
#     action = dict_1['action']
#     date = datetime.datetime.now()
#     price_objet = mt5.symbol_info_tick(symbol)


#     # Crear la solicitud de orden pendiente
#     request = {
#         'action': action,
#         'symbol': symbol,
#         'volume': lot,
#         # 'type': type_oper,
#         'price': price,
#         'sl': sl,
#         'tp': tp,
#         'comment': comentario
#     }

#     # limit (buy_limit = 2 or sell_limit = 3)
#     if dict_1['type'] == 'buy':
#         request['type'] = 2
#     elif dict_1['type'] == 'sell':
#         request['type'] = 3

#     # type_oper = operation_type()
#     #print(f'type oper: {type_oper}')

#     print('\n')
#     print(request)

#     # Enviar la orden
#     result = mt5.order_send(request)
#     print(mt5.last_error())
#     print(f'result: {result}')


#     # stop (buy_stop = 4 or sell_stop = 5)
#     if dict_1['type'] == 'buy':
#         request['type'] = 4
#     elif dict_1['type'] == 'sell':
#         request['type'] = 5

#     # type_oper = operation_type()
#     #print(f'type oper: {type_oper}')

#     print('\n')
#     print(request)

#     # Enviar la orden
#     result = mt5.order_send(request)
#     print(mt5.last_error())
#     print(f'result: {result}')


# initialize()

# def load_pickle_file(file_name):
#     loaded_data = None
#     if os.path.exists(file_name):
#         with open(file_name, "rb") as archivo:
#             loaded_data = pickle.load(archivo)
#     return loaded_data

# def delete_file(file_name):
#     if os.path.exists(file_name):
#         os.remove(file_name)
#         print(f"El archivo '{file_name}' ha sido eliminado.")
#     # else:
#         # print(f"El archivo '{file_name}' no existe.")

# def process_loaded_data(data):
#     for dict_1 in data:
#         slave(dict_1)


# file_name = "cambios.pk"
# while True:
#     # Cargamos el archivo pickle del master si existe
    
#     try:
#         loaded_data = load_pickle_file(file_name)

#         # Procesamos los datos cargados si existen
#         if loaded_data:
#             process_loaded_data(loaded_data)
#             print('pickle cargado de fomra exitosa.')

#         # Eliminamos el archivo si existe
#         delete_file(file_name)
#     except Exception as error:
#         print(error)
#         pass

#     # time.sleep(0.5)