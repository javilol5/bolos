import pytest
from src.scoreCard import ScoreCard

def test_get_strike():
    PINS = "1X345123451234512345"
    card = ScoreCard(PINS)
    total = 75
    assert card
    assert card.get_total() == total
    
#def test_get_multi_strike_one():
#    PINS = "X3451234512x451234"  
#    card = ScoreCard(PINS)
#    total = 85
#    assert card
#    assert card.get_total() == total
    
#def test_get_multi_strike_two():
#    PINS = "XXXXXXXXXXXX"  
#    card = ScoreCard(PINS)
#    total = 300
#    assert card
#    assert card.get_total() == total