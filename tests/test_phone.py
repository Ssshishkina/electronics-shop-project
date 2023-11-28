import pytest


from src.item import Item
from src.phone import Phone


def test_phone():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2


@pytest.fixture
def phone1():
    """создаем экземпляр класса в фикстуре"""
    return Phone("iPhone 14", 120_000, 5, 2)


def test_str(phone1):
    """тест для __str__"""
    assert str(phone1) == 'iPhone 14'


def test_repr(phone1):
    """тест для __repr__"""
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_add(phone1):
    """тест для __add__"""
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1.quantity + phone1.quantity == 25
    assert item1.price + phone1.price == 130000
    assert phone1.quantity + phone1.quantity == 10


def test_number_of_sim_setter():
    """проверка количества сим-карт"""
    phone = Phone("test1", 120000, 5, 2)
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2
    phone1 = Phone("iPhone 14", 120000, 5, 2)

    #ValueError: количество физических сим-карт должно быть целым числом больше нуля
    #assert phone1.number_of_sim == 0