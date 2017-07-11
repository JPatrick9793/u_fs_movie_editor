"""
Import necessary libraries:
    fresh_tomatoes for open_movies_page()
    media for class Movie
"""
import fresh_tomatoes
import media

# Initialize object "toystory" with the following parameters
toystory = media.Movie("Toy Story",
                       "A story of a boy and his toys that come to life",
                       "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",  # noqa
                       "https://youtu.be/4KPTXpQehio")

# Initialize object "avatar" with the following parameters
avatar = media.Movie("Avator",
                     "A marine on an alien planet",
                     "http://www.impawards.com/2009/posters/avatar_xlg.jpg",  # noqa
                     "https://youtu.be/cRdxXPV9GNQ")

# Initialize object "boondocksaints" with the following parameters
boondocksaints = media.Movie("Boondock Saints",
                             "Two irish twin brothers take justice into their own hands...",  # noqa
                             "https://images-na.ssl-images-amazon.com/images/I/51SfCKlDQoL._SY300_.jpg",  # noqa
                             "https://youtu.be/ydXojYfCF3I")

# Initialize object "ip_man" with the following parameters
ip_man = media.Movie("IP Man",
                     "When Japan invaded China in 1938, one Grandmaster refused to lose his honor...",  # noqa
                     "http://img.moviepostershop.com/ip-man-movie-poster-2008-1020698460.jpg",  # noqa
                     "https://youtu.be/QLy7gIH1FeA")

# create a list of objects from class Movie
# to be passed into the open_movies_page function
movies = (boondocksaints, ip_man, toystory, avatar)

# Call fresh_tomatoes to create a website using the list "movies"
fresh_tomatoes.open_movies_page(movies)