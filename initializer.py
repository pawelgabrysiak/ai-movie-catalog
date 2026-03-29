from user import User
from movie import FictionMovie, NonFictionMovie

class Initializer:

    @staticmethod
    def init_users():
        user1 = User('Paweł', 20)
        user2 = User('Anna', 25)
        user3 = User('Marek', 17)
        user4 = User('Katarzyna', 30)
        user5 = User('Olaf', 12)
        user6 = User('Małgorzata', 45)

        users = [user1, user2, user3, user4, user5, user6]
        return users

    @staticmethod
    def init_books():
        movie1 = NonFictionMovie('Ćpałem Chlałem i przetrwałem', 'Maciej Maleńczuk', True, 'Biografia Macieja Maleńczuka',
                               'Łatwy')
        movie2 = NonFictionMovie('Diego - Bóg futbolu', 'Ferrer Julio', True, 'Biografia Diego Maradony', 'Łatwy')
        movie3 = NonFictionMovie('Mike Tyson - Moja prawda', 'Larry Slowman', True, "Biografia Mike'a Tysona", 'Łatwy')
        movie4 = FictionMovie('Wiedźmin: Ostatnie życzenie', 'Andrzej Sapkowski', True, "Fantasy",
                            'Geralt zmaga się z wyzwaniami moralnymi i dylematami')
        movie5 = FictionMovie('Diuna', 'Frank Herbert', True, 'Science Fiction',
                            '"Diuna" to epicka powieść science fiction autorstwa Franka Herberta, osadzona w odległej przyszłości, gdzie polityczne intrygi, religijne proroctwa i walka o kontrolę nad cenną przyprawą melanż splatają się w fascynującą narrację.')
        movie6 = FictionMovie('Władca Pierścieni: Drużyna Pierścienia', 'J.R.R. Tolkien', True, 'Fantasy',
                            'Frodo, w towarzystwie Drużyny Pierścienia, składającej się z przedstawicieli różnych ras, wyrusza w niebezpieczną podróż, aby zniszczyć pierścień w ogniu Góry Zagłady, gdzie został wykuty.')

        movies = [movie1, movie2, movie3, movie4, movie5, movie6]
        return movies