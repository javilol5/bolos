
class ScoreCard:

    def __init__(self, scoreCard):
        self.pins = scoreCard
        self.nothing = "-"
        self.strike = "x"
        self.slash = "/"

    def get_pins(self):
        return self.pins
    
    def get_total(self):
        
        if self.nothing in self.pins:
            newPins = self.pins.replace(self.nothing, "0")
            return sum([int(pin) for pin in newPins])
        
        if self.strike in self.pins:
            posicion_de_x = self.pins.index("x")
            primer_numero = self.pins[posicion_de_x+1]
            segundo_numero = self.pins[posicion_de_x+2]
            newPins = self.pins.replace(self.strike, "55")
            return sum([int(pin) for pin in newPins]) + int(primer_numero) + int(segundo_numero)
        
        if self.slash in self.pins:
            posicion_de_slash = self.pins.index("/")
            primer_numero = self.pins[posicion_de_slash+1]
            numero_slash = 10 - int(self.pins[posicion_de_slash-1])
            newPins = self.pins.replace(self.slash, str(numero_slash))
            newPins += str(primer_numero)
            return sum([int(pin) for pin in newPins])
        
        puntos = [int(pin) for pin in self.pins]
        return sum(puntos)