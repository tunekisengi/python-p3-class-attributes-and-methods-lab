class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # increment total song count
        type(self).count += 1

        # add genre to genres list if not already present
        if genre not in type(self).genres:
            type(self).genres.append(genre)

        # add artist to artists list if not already present
        if artist not in type(self).artists:
            type(self).artists.append(artist)

        # count songs by genre
        if genre in type(self).genre_count:
            type(self).genre_count[genre] += 1
        else:
            type(self).genre_count[genre] = 1

        # count songs by artist
        if artist in type(self).artist_count:
            type(self).artist_count[artist] += 1
        else:
            type(self).artist_count[artist] = 1
