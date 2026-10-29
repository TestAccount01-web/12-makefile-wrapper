from app.pricing import cart_total


def test_cart_total(sample_items):
    assert cart_total(sample_items) == 25.5
