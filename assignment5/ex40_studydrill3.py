class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def shout_the_lyrics(self):
        for line in self.lyrics:
            print(line.upper())

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

new_york_new_york = Song(["Start spreading the news",
                        "I'm leaving today",
                        "I want to be a part of it",
                        "New York, New York"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

new_york_new_york.shout_the_lyrics()
