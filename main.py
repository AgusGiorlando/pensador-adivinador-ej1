from pensador import Pensador

# Inicializacion del Pensador
pensador = Pensador()
pensador.setNumero()

while True:
    # Ingreso por teclado
    try:
        respuesta = list(str(input("Ingresa un numero de 4 cifras: ")))
    except NameError:
        print('ERROR: El valor ingresado no es un numero')

    # ELIMINAR
    if respuesta == 0000:
        pensador.showNumero()
        break
        
    # Analisis de la entrada
    resultado = pensador.analizeRespuesta(respuesta)

    # Respuesta
    if resultado == (4, 0):
        print('Ganaste!')
        break
    else:
        print('G: %d, R: %d' % (resultado[0], resultado[1]))

print('Juego terminado')