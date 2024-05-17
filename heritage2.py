class Film:
    def __init__(self, name):
        self.name = name
    def watch(self):
        print("Bon visionnage !")
class FilmCassette(Film):
    def __init__(self, name):
        self.name = name
        self.mangetic_tape = True
    def rewind(self):
        print("c'est long a rembobiner ")
        self.mangetic_tape = True

film = Film("2001: l'odyssee de l'espace")
film_cassette = FilmCassette("Blader Runner")

print(film_cassette.name)
print(film_cassette.mangetic_tape)
film_cassette.watch()
film_cassette.rewind()