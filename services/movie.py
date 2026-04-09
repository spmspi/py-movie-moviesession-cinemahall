from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids=None, actors_ids=None) -> QuerySet:
    if genres_ids and actors_ids:
        return Movie.objects.filter(genres__in=genres_ids, actors__in=actors_ids)
    if genres_ids:
        return Movie.objects.filter(genres__in=genres_ids)
    if actors_ids:
        return Movie.objects.filter(actors__in=actors_ids)

    return Movie.objects.all()


def get_movie_by_id(movie_id) -> QuerySet[Movie]:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title, movie_description, genres_ids=None, actors_ids=None) -> QuerySet[Movie]:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    movie.save()

    return movie
