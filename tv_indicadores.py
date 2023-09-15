# import time
# import json
# from datos_divisas import variables_divisas

# from tradingview_ta import TA_Handler, Interval, Exchange, TradingView

# # Abre el archivo JSON
# with open('divisa_test.json', 'r') as archivo:
#     # Carga el contenido del archivo en una lista de diccionarios
#     divisas = json.load(archivo)

# # Guarda los archivos en un JSON
# # with open('divisas_con_intervalo.json', 'w') as archivo_salida:
# #     json.dump(divisas, archivo_salida, indent=4)

# # Este valor es variable dependiendo del tamaño de la vela...
# num = 0
# # inicio = time.time()

# Interval = ['5m', '15m', '30m']


# for i in range(5):
#     if num < 5:
#         for x in range(len(Interval)):
#         # print(Interval[x])
#         # Interval = Interval.INTERVAL_1_MINUTE
#             print(variables_divisas(divisas, Interval[x]))
#         print()
#         time.sleep(30)
#     num += 1

