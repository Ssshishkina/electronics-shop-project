import csv
import os
os.path.join('src', 'items.csv')


class Item:
    """ Класс для представления товара в магазине."""
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, filename) -> None:
        Item.all.clear()
        with open(filename, newline='', encoding='windows-1251') as csvfile:
            file_reader = list(csv.DictReader(csvfile, delimiter = ","))
            for line in file_reader:
                name = line['name']
                price = int(line['price'])
                quantity = int(line['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(num_string: str) -> int:
        return int(float(num_string))

    def calculate_total_price(self) -> float:
        """Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара."""
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара."""
        self.price *= self.pay_rate
