from rest_framework import generics
from movies.models import Movie
from movies.api.v1.serializers import MovieSerializer


class MovieAPIView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Movie.objects.order_by("-ranking")
    serializer_class = MovieSerializer
