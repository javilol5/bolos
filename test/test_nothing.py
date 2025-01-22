import pytest
from src.scoreCard import ScoreCard

def test_get_nothing_one():
    PINS = "9-9-9-9-9-9-9-9-9-9-"
    card = ScoreCard(PINS)
    total = 90
    assert card
    assert card.get_total() == total

def test_get_nothing_two():
    PINS = "9-3561368153258-7181"
    card = ScoreCard(PINS)
    total = 72
    assert card
    assert card.get_total() == total