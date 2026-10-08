def calculate_online_order(price, quantity):
    if price < 0: return 0
    if quantity < 0: return 0
    subtotal = price * quantity
    tax = subtotal * 0.18
    total = subtotal + tax
    return round(total, 2)

def calculate_store_order(price, quantity):
    if price < 0: return 0
    if quantity < 0: return 0
    subtotal = price * quantity
    tax = subtotal * 0.18
    total = subtotal + tax
    return round(total, 2)

def calculate_partner_order(price, quantity):
    if price < 0: return 0
    if quantity < 0: return 0
    subtotal = price * quantity
    tax = subtotal * 0.18
    total = subtotal + tax
    return round(total, 2)
