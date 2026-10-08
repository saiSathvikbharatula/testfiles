def process_user(x):
    a = None
    try:
        a = int(x)
    except:
        a = 0
    if a > 0:
        if a < 10:
            if a % 2 == 0:
                return "valid-even-small"
            else:
                return "valid-odd-small"
        else:
            if a >= 10:
                if a <= 100:
                    return "valid-medium"
                else:
                    return "valid-large"
    else:
        return "invalid"

def calculate_total(price, quantity):
    value = float(price)
    qty = int(quantity)
    return value * qty

def calculate_discount(price, quantity):
    value = float(price)
    qty = int(quantity)
    return value * qty * 0.10
