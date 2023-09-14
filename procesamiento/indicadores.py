import time
import json

from tradingview_ta import TA_Handler, Interval, Exchange, TradingView

def variables_divisas(divisas, Interval):# Iterar sobre el Json
    
    analisis_divisa = []

    for i in range(len(divisas)):
        # print(divisas[i])

        # valores del json
        symbol = divisas[i]['symbol']
        screener = divisas[i]['screener']
        exchange = divisas[i]['exchange']
        interval = Interval # -> varia de acuerdo a la periodicidad
    
        # funcion del API de TV
        handler = TA_Handler(symbol=symbol, screener=screener, exchange=exchange, interval=interval)
        analisis = handler.get_analysis()
        tipo = analisis.summary['RECOMMENDATION']

        if tipo == 'STRONG_SELL': tipo = 'SELL'
        if tipo == 'STRONG_BUY': tipo = 'BUY'

        close = analisis.indicators["close"]
        high = analisis.indicators["high"]
        low = analisis.indicators["low"]
        rsi = analisis.indicators["RSI"]
        cci20 = analisis.indicators["CCI20"]
        ema5 = analisis.indicators["EMA5"]
        adx = analisis.indicators["ADX"]
        ema10 = analisis.indicators["EMA10"]
        sma20 = analisis.indicators["SMA20"]
        volume = analisis.indicators["volume"]


        # Calcula el ATR basado en valores en tiempo real
        real_range = high - low
        atr_multiplier = 0.5  # Se puede ajustar según las preferencias
        atr = real_range * atr_multiplier
        
        # Ajusta los niveles de SL y TP en función de los indicadores
        if tipo == "NEUTRAL": 
            sl = close
            tp = close
        elif tipo == "BUY": # "Long"
            # Ajusta el SL y TP según el RSI
            if rsi > 70:
                sl = close - atr * 2  # Ajusta el multiplicador 
                tp = close + atr  # Ajusta el multiplicador 
            else:
                sl = close - atr  # Ajusta el multiplicador 
                tp = close + atr * 2  # Ajusta el multiplicador 
        elif tipo == "SELL": # "Short"
            # Ajusta el SL y TP según el CCI20
            if cci20 < -100:
                sl = close + atr * 2  # Ajusta el multiplicador 
                tp = close - atr  # Ajusta el multiplicador 
            else:
                sl = close + atr  # Ajusta el multiplicador 
                tp = close - atr * 2  # Ajusta el multiplicador 
        
        # print(f'symbol: {symbol}')
        # print(f'tipo: {tipo}')
        # print(f'precio: {close}')
        # print(f'high: {high}')
        # print(f'close: {close}')
        # print(f'interval: {interval}')
        # print(f'sl: {sl}')
        # print(f'tp: {tp}')
        # print('')

        i = {'symbol': symbol, 'tipo': tipo,
                'precio': close, 'high': high,
                'low': low, 'interval': interval,
                'sl': sl, 'tp': tp
            }
        
        analisis_divisa.append(i)

    # print(master)
    return(analisis_divisa)
    # return(symbol, tipo, close, high, close, interval, sl, tp)
    

# variables_divisas()

