from utils.validators import valid_percentage, valid_roll_number

def test_percentage():
    assert valid_percentage(80)
    assert not valid_percentage(120)

def test_roll():
    assert valid_roll_number("24BCE0001")
    assert not valid_roll_number(" ")
