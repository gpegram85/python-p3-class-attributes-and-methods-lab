class Song:

    count = 0
    songs = []
    artists = []
    artist_count = {}
    genres = []
    genre_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_song_name(name)
        Song.add_to_artists(artist)
        Song.add_to_genres(genre)
        

    @classmethod
    def add_song_name(cls, song_name):
        cls.songs.append(song_name)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def show_song_count(cls):
        print(cls.count)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
        cls.add_to_artist_count(artist)

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    @classmethod
    def show_artists_names(cls):
        print([artist for artist in cls.artists])

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        cls.add_to_genre_count(genre)

    
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1