
class ScoreCard:

    def __init__(self, scoreCard):
        self.pins = scoreCard

    def get_pins(self):
        return self.pins
    
    def get_total(self):
        RAYA = "-"
        EQUIS = "x"
        
        if RAYA in self.pins:
            newPins = self.pins.replace(RAYA, "0")
            return sum([int(pin) for pin in newPins])
        
        if EQUIS in self.pins:
            posicion_de_x = self.pins.index("x")
            primer_numero = self.pins[posicion_de_x+1]
            segundo_numero = self.pins[posicion_de_x+2]
            newPins = self.pins.replace(EQUIS, "55")
            return sum([int(pin) for pin in newPins]) + int(primer_numero) + int(segundo_numero)
            
        puntos = [int(pin) for pin in self.pins]
        return sum(puntos)