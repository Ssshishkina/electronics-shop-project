from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        '''Сoздан новый класс 'Phone' с атрибутами класса Item
        и доп.атрибутом - колличество поддерживаемых сим-карт'''

        # расширяем функционал через super(), вызовом __init__ род.класса
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        """Метод реализации оператора сложения экземпляров класса
        'Phone' и 'Item' по количеству товара в магазине"""
        if not isinstance(other, Item):
            raise ValueError("нельзя сложить 'Phone' или 'Item' с экземплярами не 'Phone' или 'Item' классов")
        return self.quantity + other.quantity


    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num_sim):
        if not isinstance(num_sim, int) or num_sim <= 0:
            raise ValueError('количество физических sim-карт должно быть целым числом больше нуля')
        self.__number_of_sim = num_sim


