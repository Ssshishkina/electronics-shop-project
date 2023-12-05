from src.item import Item

class MixinLanguage:
    def __int__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language.upper() == 'EN':
            self.__language = 'RU'
            return self
        if self.__language.upper() == 'RU':
            self.__language = 'EN'
        return self

class Keyboard(MixinLanguage, Item):
    pass
