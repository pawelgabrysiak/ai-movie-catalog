from abc import ABC, abstractmethod


class Movie(ABC):
    def __init__(self, title, author, available=True):
        self.available = available
        self.title = title
        self.author = author

    @abstractmethod
    def display_concrete_info(self):
        pass

    def display_movie_info(self):
        print(f'(Nazwa : {self.title}')
        print(f'Autor : {self.author}')
        self.display_concrete_info()
        print(f"Dostępna? : {'Tak' if self.available else 'Nie'}")

    def __repr__(self):
        return f'(Nazwa : {self.title}, Autor : {self.author}, Avaible : {self.available})'


class NonFictionMovie(Movie):
    def __init__(self, title, author, available, subject, level):
        super().__init__(title, author, available)
        self.subject = subject
        self.level = level

    def display_concrete_info(self):
        print(f'(Temat : {self.subject})')
        print(f'(Poziom : {self.level})')


class FictionMovie(Movie):
    def __init__(self, title, author, available, genre, synopsis):
        super().__init__(title, author, available)
        self.genre = genre
        self.synopsis = synopsis

    def display_concrete_info(self):
        print(f'(Gatunek : {self.genre})')
        print(f'(Streszczenie : {self.synopsis})')


class MovieNotFoundError(Exception):
    pass


class MovieNotAvailableError(Exception):
    pass
