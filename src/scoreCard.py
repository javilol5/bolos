
class ScoreCard:

    def __init__(self, scoreCard):
        self.pins = scoreCard
        self.LAST_FRAME = 10
        self.frame = 1
        self.score = 0

    def frame_pins(self, roll):
        frame_pins = self.pins[roll]
        if frame_pins not in ['/', 'X']:
            frame_pins += self.pins[roll + 1]
            roll += 1
        return roll, frame_pins

    def get_pins(self):
        return self.pins
    
    def get_total(self):
        RAYA = "-"
        total = []
        
        if RAYA in self.pins:
            for pin in self.pins:
                if pin == '-':
                    total.append(0)
                    print("Yeah")
                else:
                    total.append(pin)
                    print("Yeah")
        print(total)
        puntos = [int(element) for element in total]
        return sum(puntos)
    
