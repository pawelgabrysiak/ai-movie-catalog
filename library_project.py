import sys

from movie import MovieNotFoundError, MovieNotAvailableError
from initializer import Initializer 
from library import MovieCatalog
from user import UserNotFound


if __name__ == '__main__':
    
    # inicjalizacja danych (docelowo tutaj wjedzie Pandas i pliki JSON)
    users = Initializer.init_users()
    movies = Initializer.init_books()
    catalog = MovieCatalog(users, movies)
    current_user = None

    print("Witaj w Movie Catalog!")

    while True:
        try:
            while current_user is None:
                name = input("Podaj login (nazwę użytkownika):\n")
                current_user = catalog.login(name)

            print("\n--- MENU GŁÓWNE ---")
            print("1 - Wyświetlanie wszystkich filmów w katalogu")
            print("2 - Wyświetlanie Twojej listy 'Do obejrzenia' (Watchlist)")
            print("3 - Dodanie filmu do listy 'Do obejrzenia'")
            print("4 - Oznaczenie filmu jako obejrzany (Usunięcie z listy)")
            print("5 - Wyloguj się")
            print("6 - Wyjście")
            option = int(input("Wybierz opcję, którą chcesz zrealizować:\n"))

            if option == 6:
                print("Do widzenia!")
                sys.exit()

            elif option == 1:
                catalog.print_all_movies()

            elif option == 2:
                catalog.print_watchlist(current_user=current_user)

            elif option == 3:
                title_of_movie = input('Podaj tytuł filmu, który chcesz dodać do listy:\n')
                catalog.add_to_watchlist(title_of_movie, current_user=current_user)

            elif option == 4:
                title_of_movie = input('Podaj tytuł filmu, który obejrzałeś (zostanie usunięty z listy):\n')
                catalog.remove_from_watchlist(title_of_movie, current_user=current_user)

            elif option == 5:
                current_user = None
                print('Wylogowano pomyślnie!')

            else:
                raise ValueError('Nieprawidłowy numer opcji. Wybierz cyfrę od 1 do 6.')
                
        except ValueError as e:
            print(f"Błąd: {e}")
        except MovieNotFoundError as e:
            print(f"Błąd: {e}")
        except MovieNotAvailableError as e:
            print(f"Błąd: {e}")
        except UserNotFound as e:
            print(f"Błąd: {e}")