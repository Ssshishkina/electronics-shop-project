"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

def test_item():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20
    assert item1.calculate_total_price() == 200000
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000

    item2 = Item("Ноутбук", 20000, 5)
    assert item2.name == "Ноутбук"
    assert item2.price == 20000
    assert item2.quantity == 5
    assert item2.calculate_total_price() == 100000
    Item.pay_rate = 0.8
    item2.apply_discount()
    assert item2.price == 16000
    assert Item.all == [item1, item2]
