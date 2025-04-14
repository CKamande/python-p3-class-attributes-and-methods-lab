class Song:
    # Class-level attributes to track the count of songs, genres, and artists
    count = 0
    genre_count = {}
    artist_count = {}
    genres = set()
    artists = set()

    def __init__(self, name, artist, genre):  
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the total song count
        Song.count += 1

        # Update genre count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Update artist count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

        # Add the genre and artist to the set of genres and artists
        Song.genres.add(genre)
        Song.artists.add(artist)

    def __str__(self):
        return f"'{self.name}' by {self.artist} ({self.genre})"

    def is_valid_genre(self, valid_genres=None):
        """Check if the genre is valid."""
        if valid_genres is None:
            valid_genres = ["Pop", "Rock", "Hip-Hop", "Rap", "Jazz", "Classical", "Electronic"]
        return self.genre in valid_genres

    def get_song_details(self):
        """Return the song's details in a formatted string."""
        return f"Song: {self.name}, Artist: {self.artist}, Genre: {self.genre}"
