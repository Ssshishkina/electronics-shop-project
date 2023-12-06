from src.item import Item


class MixinLanguage:
    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def __str__(self):
        return self.__language

    def change_lang(self):
        if self.__language.upper() == 'EN':
            self.__language = 'RU'
            return self.__language
        elif self.__language.upper() == 'RU':
            self.__language = 'EN'
            return self.__language


class Keyboard(Item, MixinLanguage):
    pass
