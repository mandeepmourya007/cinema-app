from celery import shared_task
from .models import Movie
from datetime import timedelta

@shared_task
def update_movie_rankings():
    movies = Movie.objects.filter(status__in=['coming_up','starting','starting'])
    for movie in movies:
        movie.ranking += 10
        movie.save()
