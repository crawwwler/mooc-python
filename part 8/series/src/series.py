class Series:

    def __init__(self, title: str, season: int, genres: list):
        self.title = title
        self.season = season
        self.genres = genres
        self.rating = []

    
    def __str__(self):
        genres_str = ', '.join(self.genres)
        if len(self.rating) == 0 :
            rates = 'no ratings'
        else:
            rates = f"{len(self.rating)} ratings, average {(sum(self.rating) / len(self.rating)):.1f} points"

        return f"{self.title} ({self.season} seasons)\ngenres: {genres_str}\n{rates}"


    def rate(self, rating: int):
        if 0 <= rating <= 5 :
            self.rating.append(rating)
    
    def stars(self):
        return sum(self.rating) / len(self.rating)


def minimum_grade(rating: float, series_list: list):
    list_to_return = []
    for serie in series_list :
        if serie.stars() >= rating :
            list_to_return.append(serie)
    return list_to_return


def includes_genre(genre: str, series_list: list):
    list_to_return = []
    for serie in series_list:
        if genre in serie.genres :
            list_to_return.append(serie)
    return list_to_return

