from db.models import Movie, Genre, Actor


def get_movies(
    genres_ids: list | None = None,
    actors_ids: list | None = None
) -> Movie:

    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genres__id__in=genres_ids, actors__id__in=actors_ids)

    if genres_ids and not actors_ids:
        return Movie.objects.filter(
            genres__id__in=genres_ids)

    if actors_ids and not genres_ids:
        return Movie.objects.filter(
            actors__id__in=actors_ids)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list | None = None,
    actors_ids: list | None = None
) -> Movie:

    movie = Movie.objects.create(
        title=movie_title, description=movie_description)
    if genres_ids:
        movie.genres.set(Genre.objects.filter(id__in=genres_ids))
    if actors_ids:
        movie.actors.set(Actor.objects.filter(id__in=actors_ids))
    return movie
