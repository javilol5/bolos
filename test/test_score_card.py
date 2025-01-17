import pytest
from src.scoreCard import ScoreCard

def test_score_card():
    card = ScoreCard("12345123451234512345")
    assert card

def test_get_pins():
    PINS = "12345123451234512345"
    card = ScoreCard(PINS)
    assert card
    assert card.get_pins() == PINS

def test_get_total():
    PINS = "12345123451234512345"
    card = ScoreCard(PINS)
    total = 60
    assert card
    assert card.get_total() == total

def test_get_nothing():
    PINS = "1-345123451234512345"
    card = ScoreCard(PINS)
    total = 58
    assert card
    assert card.get_total() == total

def test_get_strike():
    PINS = "1x345123451234512345"
    card = ScoreCard(PINS)
    total = 75
    assert card
    assert card.get_total() == total

def test_get_semi():
    PINS = "1/ 34 51 23 45 12 34 51 23 45"
    card = ScoreCard(PINS)
    total = 70
    assert card
    assert card.get_total() == total

def test_get_multi_nothing():
    PINS = "1-3451234-12345-2345"
    card = ScoreCard(PINS)
    total = 52
    assert card
    assert card.get_total() == total

#def test_get_multi_strike():
#    PINS = "x3451234512x451234"
#    card = ScoreCard(PINS)
#    total = 85
#    assert card
#    assert card.get_total() == total
#
#def test_get_multi_semi():
#    PINS = "1/345123451/34512345"
#    card = ScoreCard(PINS)
#    total = 80
#    assert card
#    assert card.get_total() == total

def test_get_nothing_together():
    PINS = "1--45123451234512345"
    card = ScoreCard(PINS)
    total = 55
    assert card
    assert card.get_total() == total

#def test_get_strike_together():
#    PINS = "14 x x 51 23 45 12 34 51 23"
#    card = ScoreCard(PINS)
#    total = 87
#    assert card
#    assert card.get_total() == total