from movie import NonFictionMovie, FictionMovie, MovieNotFoundError, MovieNotAvailableError
# Kompozycja - klasa MovieCatalog składa się z obiektów User i Movie
from user import UserNotFound

class MovieCatalog:
    def __init__(self, users, movies):
        self.users = users
        self.movies = movies

    def login(self, name):
        for user in self.users:
            if name == user.name:
                print("\nZalogowano pomyślnie!")
                print(f"Twoje dane: {user}")
                return user
        raise UserNotFound('Niepoprawny login. Użytkownik nie istnieje.')

    def add_to_watchlist(self, movie_title, current_user):
        for movie in self.movies:
            if movie_title == movie.title:
                if movie in current_user.watchlist:
                    raise MovieNotAvailableError("Ten film jest już na Twojej liście do obejrzenia!")
                
                current_user.watchlist.append(movie)
                print(f"Sukces! Dodano '{movie.title}' do Twojej listy.")
                return
                
        raise MovieNotFoundError("Proszę podać prawidłowy tytuł filmu z katalogu!")

    def remove_from_watchlist(self, title_of_movie, current_user):
        for movie in current_user.watchlist:
            if title_of_movie == movie.title:
                current_user.watchlist.remove(movie)
                print(f"Film '{movie.title}' został oznaczony jako obejrzany i usunięty z listy.")
                return
                
        raise MovieNotFoundError("Nie masz takiego filmu na swojej liście do obejrzenia!")

    def print_watchlist(self, current_user):
        if len(current_user.watchlist) > 0:
            print('\nTwoja lista do obejrzenia:')
            for movie in current_user.watchlist:
                movie.display_movie_info()
            return
        print('\nBrak filmów na liście do obejrzenia.')

    def print_all_movies(self):
        print('\nKatalog wszystkich filmów:')
        for movie in self.movies:
            movie.display_movie_info()