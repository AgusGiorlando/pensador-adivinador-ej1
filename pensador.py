import random

class Pensador:
    """ Genera un numero de 4 cifras aleatorias que no se repiten """
    
    def __init__(self):
        self.numero = list()

    def setNumero(self):
        while len(self.numero) < 4:
            cifra = random.randint(0, 9)
            if self.numero.count(str(cifra)) == 0:
                self.numero.append(str(cifra))
            

    def showNumero(self):
        print("numero:")
        print(self.numero)

    def analizeRespuesta(self, respuesta):
        g = 0
        r = 0
        
        for cifra in respuesta:
            try:
                if self.numero.index(str(cifra)) == respuesta.index(str(cifra)):
                    g += 1
                else:
                    r += 1
            except ValueError:
                pass

        return (g, r)