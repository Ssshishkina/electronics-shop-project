"""Здесь надо написать тесты с использованием pytest для модуля item."""
import os
import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone
os.path.join('src', 'items.csv')


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


def test_repr():
    """Тест для __repr__"""
    item1 = Item("Смартфон, 1000, 20")
    assert repr(item1) == "Item('Смартфон', 1000, 20)"


def test_str():
    """Тест для __str__"""
    item1 = Item('Смартфон, 1000, 20')
    assert str(item1) == 'Смартфон'


def test_instantiate_from_csv():
    Item.instantiate_from_csv("src/items.csv")
    assert len(Item.all) == 5
    assert Item.all[1].name == "Ноутбук"
    assert Item.all[2].price == 10
    assert Item.all[4].quantity == 5


def test_instantiate_from_csv_file_not():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(os.path.join('..', 'src', 'somefile.csv'))


def test_instantiate_from_csv_file_error():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(os.path.join('..', 'tests', 'test_items.csv'))


def test_string_to_number():
    """Тест для вспомогательного метода tring_to_number"""
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.5") == 5
