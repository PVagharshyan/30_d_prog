from artists import Artist
from playlist import Playlist
from songs import Song
from users import User
from music_platform import MusicPlatform, RockSong, PopSong

if __name__ == "__main__":
    platform = MusicPlatform()

    artist1 = Artist("John Doe", "johndoe@example.com")
    artist2 = Artist("Jane Smith", "janesmith@example.com")

    song1 = RockSong("Rock Song 1", artist1, 240, "Classic Rock")
    song2 = PopSong("Pop Song 1", artist2, 180, "Happy Pop")

    platform.add_song(song1)
    platform.add_song(song2)

    user1 = User("User1", "user1@example.com")
    user1.add_favorite_song(song1)
    user1.add_favorite_artist(artist1)

    searched_song = platform.search_song("Rock Song")
    if searched_song:
        print(f"Found song: {searched_song.title} by {searched_song.artist.name}")
    else:
        print("Song not found.")

    discovered_artists = platform.discover_artist()
    print("Discovered artists:")
    for artist in discovered_artists:
        print(artist.name)
