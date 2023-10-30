from movies import Movie
from theaters import Theater,StandardTheater,IMAXTheater
from showtimes import Showtime
from movie_theater import MovieTheaterSystem, MovieTheater

def main():
    movie1 = Movie("Inception", "Sci-Fi", 148)
    movie2 = Movie("The Dark Knight", "Action", 152)
    standard_theater = StandardTheater("Location A", 100)
    imax_theater = IMAXTheater("Location B", 50)
    showtime1 = Showtime(movie1, standard_theater, "2023-10-31 19:00")
    showtime2 = Showtime(movie2, imax_theater, "2023-11-01 15:00")

    movie_theater_system = MovieTheaterSystem()
    movie_theater_system.movies = [movie1, movie2]
    movie_theater_system.showtimes = [showtime1, showtime2]

    movies_list = movie_theater_system.browse_movies()
    showtimes_list = movie_theater_system.browse_showtimes()

if __name__ == "__main__":
    main()
