class Film:
    def __init__(self, name):
        self.name = name

    def watch(self):
        print("Bon visionnage !")

class FilmCassette(Film):
    pass
film = Film("2001: l'odyssee de l'espace")
filme_cassette = FilmCassette("Blader Runner")

film.name
film.watch()

filme_cassette.name
filme_cassette.watch()