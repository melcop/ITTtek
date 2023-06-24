import mystuff
class MyStuff(object): 
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

print(mystuff.tangerine)
mystuff= mystuff.apple()
mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

thing = MyStuff()
thing.apple()
print(thing.tangerine)

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
"With pockets full of shells"])
heavy_metal = Song(["It's dark everywhere",
"And there is blood everywhere", "I don't give a shit of anybody",
"So, fuck off!"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
print("----------------------------------\n")
heavy_metal.sing_me_a_song()
print("----------------------------------\n")