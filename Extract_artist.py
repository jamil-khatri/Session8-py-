def extract_artist(song_title):
    dash = song_title.index("-")
    artist = song_title[dash + 1:]
    return artist.strip()


song = input("Enter song name and artist: ")
print("Artist:", extract_artist(song))
