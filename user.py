class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.watchlist = []

    def __repr__(self):
        return f'({self.name}, {self.age} lat)'

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age >= 0:
            self._age = age
        else:
            raise ValueError('Invalid age')


class UserNotFound(Exception):
    pass
