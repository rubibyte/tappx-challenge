class GotCharacter:
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if not isinstance(first_name, str):
            raise TypeError("first name must be a string")
        self._first_name = first_name

    @property
    def is_alive(self):
        return self._is_alive

    @is_alive.setter
    def is_alive(self, is_alive):
        if not isinstance(is_alive, bool):
            raise TypeError("is_alive must be of type boolean: True or False")
        self._is_alive = is_alive


class Stark(GotCharacter):
    '''A class representing the Stark family. Or when bad things happen to \
good people.'''
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self._family_name = "Stark"
        self._house_words = "Winter is Coming"

    @property
    def family_name(self):
        return self._family_name

    @property
    def house_words(self):
        return self._house_words

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
