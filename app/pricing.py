def apply_discount(price, pct):
    return round(price * (1 - pct / 100), 2)


def cart_total(items):
    return round(sum(i['price'] * i['qty'] for i in items), 2)
