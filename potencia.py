import sys
class Lenguaje():
                            
    def __init__(self,lenguaje):        
        self.lenguaje = lenguaje
        self.palabras = 1
        
        for i in range(len(self.lenguaje)):
            if(self.lenguaje[i] == ","):
                self.palabras += 1
        print("llega hsta aquí")
    
    def palabraDesde(pos):
        tamano = len(self.lenguaje)
        for i in range(len(self.lenguaje[pos:tamano])):
            if(self.lenguaje[i] == "," or self.lenguaje[i] == "}"):
                palabra = self.lenguaje[pos:i]
                break
                return palabra


objeto = Lenguaje("{bo,be,vi,ni}")
print(objeto.palabras)

