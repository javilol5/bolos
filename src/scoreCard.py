class ScoreCard:
    
    MAX_VALUE = 10

    def __init__(self, scoreCard):
        self.pins = scoreCard
        self.nothing = "-"
        self.strike = "X"
        self.slash = "/"

    def get_pins(self):
        return self.pins
    
    def get_total(self):
        '''''''''
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
        '''
        newPins = []
        for position_pin, pin in enumerate(self.pins):
            

            if pin == self.nothing:
                newPins.append("0")
                print(newPins)
                self.pins.replace(self.nothing, "0")
                print(newPins)
            if pin == self.strike:
                #primer_numero = self.pins[position_pin+1]
                #segundo_numero = self.pins[position_pin+2]
                #newPins.append(str(ScoreCard.MAX_VALUE))
                #newPins.append(primer_numero)
                #newPins.append(segundo_numero)

                newPins.append('55')
                print(newPins)
                if position_pin + 1 < len(self.pins):
                    newPins.append(int(self.pins[position_pin + 1]))
                    print(newPins)
                if position_pin + 2 < len(self.pins):
                    newPins.append(int(self.pins[position_pin + 2]))
                    print(newPins)
            
            elif pin == self.slash:
                #primer_numero = self.pins[position_pin+1]
                #numero_slash = ScoreCard.MAX_VALUE - int(self.pins[position_pin-1])
                #newPins.append(str(numero_slash))
                #newPins.append(primer_numero)

                if position_pin > 0:
                    numero_slash = ScoreCard.MAX_VALUE - int(self.pins[position_pin - 1])
                    newPins.append(numero_slash)
                    print(newPins)
                if position_pin + 1 < len(self.pins):
                    newPins.append(int(self.pins[position_pin + 1]))
                    print(newPins)

                                                                                                            #PINS = "9- 3/ 61 3/ 81 5/ -/ 8- 7/ 8-"
            elif self.nothing in newPins:
                newPins = [elemento for elemento in newPins if elemento != '-']

            else:
                newPins.append(pin)
                print(newPins)
                

        return sum([int(pin) for pin in str(newPins) if pin.isdigit()])