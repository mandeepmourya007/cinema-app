from django.urls import path
from movies.api.v1.view import MovieAPIView
urlpatterns = [
    path('',MovieAPIView.as_view())

]