import random

class Pensador:
    def __init__(self):
        self.numero = list()

    def setNumero(self):
        while len(self.numero) < 4:
            cifra = random.randint(0, 9)
            if self.numero.count(cifra) == 0:
                self.numero.append(cifra)    
            

    def showNumero(self):
        print("numero:")
        for x in self.numero:
            print(x)