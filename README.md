Este proyecto consiste en lo siguiente:

1. Recibir diferentes parametros a traves de Trading View sobre ciertas divisas pre establecidas.
2. Con esta informacion crear un Stop Loss (SL) y Take Profit (TP).
3. Enviar esta informacion a MT5 y crear una nueva operacion.
4. La operacion puede ser tipo Long (compra) o short (Venta).
5. El bot cierra las operaciones que no se abre despues de un tiempo predeterminado.
6. Si la divisa sigue fluctuando despues de 3 ciclos (velas), se reajusta el TP y SL.


La estructura de este proyecto es la siguiente (temporal):

```console
TV_MT5_BOT/
├── main.py
├── procesamiento/
│   ├── __init__.py
│   |── indicadores.py
│   └── long_short.py
└── otros/
    ├── __init__.py
    ├── divisas.json
    └── credenciales.txt
    
```

Ahora miremos de que se compone la estructura:

### indicadores/

Contiene todos los archivos.py que se encargan de recolectar la informacion de las divisas

- `indicadores/_init__.py`: Archivo requerido para hacer que Python reconozca los archivos que contiene el directio como paquetes de un módulo.
- `indicadores/indicadores.py`: Este archivo realiza todo el procesamiento requerido para obtener los indicadores de las divisas.
- `long_short.py`: Este archivo envia las ordenes a MT5 para abrir operaciones de forma automatica.

### otros/

Contiene todos los archivos.py que se encargan de recolectar la informacion de las divisas

- `otros/_init__.py`: Archivo requerido para hacer que Python reconozca los archivos que contiene el directio como paquetes de un módulo.
- `otros/divisas.json`: Este archivo contiene la informacion requerida de las diferentes divisas.
- `credenciales.txt`: Este archivo contiene las credenciales para ingresar a MetaTrader5.