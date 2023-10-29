from songs import Song, Rock, Pop
from albums import Albom

def main():
    artist = ["ddd","fdsfsdf", "dadasd"]
    song1 = Song("ddd", artist, 1000, Rock())
    song2 = Song("ttt", artist, 1550, Pop())
    song3 = Song("ddas", artist, 1030, Pop())
    song4 = Song("dddaad", artist, 10666, Rock())

    a = Albom("myalbom", artist, 1960)
    songs = [song1, song2, song3, song4]
    for i in songs:
        a.add_song(i)
    print(a.songs)

    print(a.play())

if __name__ == "__main__":
    main()
