import pytest
from src.scoreCard import ScoreCard

def test_get_slash():
    PINS = "5/5/5/5/5/5/5/5/5/5/5"
    card = ScoreCard(PINS)
    total = 150
    assert card
    assert card.get_total() == total