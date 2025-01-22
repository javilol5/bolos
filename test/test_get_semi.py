from src.scoreCard import ScoreCard

def test_get_semi_one():
    PINS = "9-3/613/815/-/8-7/8-"
    card = ScoreCard(PINS)
    total = 121
    assert card
    assert card.get_total() == total
    
#def test_get_semi_two():
#    PINS = "X9-9-9-9-9-9-9-9-9-"
#    card = ScoreCard(PINS)
#    total = 100
#    assert card
#    assert card.get_total() == total
    
#def test_get_semi_three():
#    PINS = "X9-X9-9-9-9-9-9-9-"
#    card = ScoreCard(PINS)
#    total = 110
#    assert card
#    assert card.get_total() == total
    
#def test_get_semi_four():
#    PINS = "XX9-9-9-9-9-9-9-9-"
#    card = ScoreCard(PINS)
#    total = 120
#    assert card
#    assert card.get_total() == total
    
#def test_get_semi_five():
#    PINS = "XXX9-9-9-9-9-9-9-"
#    card = ScoreCard(PINS)
#    total = 141
#    assert card
#    assert card.get_total() == total

#def test_get_semi_six():
#    PINS = "9-3/613/815/-/8-7/8/8"
#    card = ScoreCard(PINS)
#    total = 131
#    assert card
#    assert card.get_total() == total
    
#def test_get_semi_multiple_strike():
#    PINS = "9-9-9-9-9-9-9-9-9-XXX"
#    card = ScoreCard(PINS)
#    total = 111
#    assert card
#    assert card.get_total() == total
