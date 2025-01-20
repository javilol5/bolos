class ScoreCard:
    
    MAX_VALUE = 10

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
            newPins = []
            
            for position_pin, pin in enumerate(self.pins):
                if pin == self.strike:
                    primer_numero = self.pins[position_pin+1]
                    segundo_numero = self.pins[position_pin+2]
                    newPins.append(str(ScoreCard.MAX_VALUE))
                    newPins.append(primer_numero)
                    newPins.append(segundo_numero)
                else:
                    newPins.append(pin) 
            return sum([int(pin) for pin in newPins])
        

        if self.slash in self.pins:
            newPins = []
            for position_pin, pin in enumerate(self.pins):
                if pin == self.slash:
                    primer_numero = self.pins[position_pin+1]
                    numero_slash = ScoreCard.MAX_VALUE - int(self.pins[position_pin-1])
                    newPins.append(str(numero_slash))
                    newPins.append(primer_numero)
                    print(newPins)
                else:
                    newPins.append(pin)
                    print(newPins)
            return sum([int(pin) for pin in str(newPins) if pin.isdigit()])


        puntos = [int(pin) for pin in self.pins]
        return sum(puntos)