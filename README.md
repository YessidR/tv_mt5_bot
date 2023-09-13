Este proyecto consiste en lo siguiente:

1. Recibir ciertos parametros a traves de Trading View sobre ciertas divisas pre establecidas.
2. Con esta informacion crear un Stop Loss (SL) y Take Profit (TP).
3. Enviar esta informacion a MT5 y crear una nueva operacion.
4. La operacion puede ser tipo Long (compra) o short (Venta).
5. El bot cierra las operaciones que no se abre despues de un tiempo predeterminado.
6. Si la divisa sigue fluctuando despues de 3 ciclos (velas), se reajusta el TP y SL.
