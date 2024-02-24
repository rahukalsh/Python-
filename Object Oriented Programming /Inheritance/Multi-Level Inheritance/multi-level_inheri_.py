#------------  Multi-Level Inheritance ---------------------

class Singer:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print(f"\nThe Singer name is {self.name} ")
    
class Song(Singer):
    def __init__(self, name, song_name, musician_name = "Pritam"):
        Singer.__init__(self, name)
        self.song_name = song_name
        self.musician_name = musician_name

    def show_details(self):
        Singer.show_details(self)
        print(f"Great {self.musician_name} is the Musician of {self.song_name} Song.\n\tWhich is sang by one and only {self.name}")

class ViMusic(Song):
    def __init__(self, name, song_name, film_name):
        Song.__init__(self, name, song_name)
        self.film_name = film_name
      
    def show_details(self):
        Song.show_details(self)
        print(f"This {self.song_name} Song is Sang by {self.name} in the {self.film_name} Film")

first_song = ViMusic("Arijit Singh", "Channa Mereya", "Ae Dil Hai Mushkil")
first_song.show_details()

second_song = ViMusic("Mohit Chauhan", "Tum Se Hi", "Jab We Met")
second_song.show_details()
