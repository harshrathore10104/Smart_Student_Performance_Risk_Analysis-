def valid_percentage(value):
    return isinstance(value, (int, float)) and 0 <= value <= 100

def valid_roll_number(value):
    return isinstance(value, str) and bool(value.strip())
