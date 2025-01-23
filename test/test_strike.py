import pytest
from src.scoreCard import ScoreCard

def test_get_strike():
    PINS = "12X4512345123451234"
    card = ScoreCard(PINS)
    total = 71
    assert card
    assert card.get_total() == total
    
def test_get_multi_strike_one():
    PINS = "X3451234512X451234"  
    card = ScoreCard(PINS)
    total = 85
    assert card
    assert card.get_total() == total
    
def test_get_multi_strike_two():
    PINS = "XXXXXXXXXXXX"  
    card = ScoreCard(PINS)
    total = 300
    assert card
    assert card.get_total() == total