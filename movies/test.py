from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Movie

class MovieTests(APITestCase):
    def test_create_movie(self):
        url = reverse('movie-create')
        data = {
            'name': 'Test Movie',
            'protagonists': 'John Doe',
            'poster': 'http://example.com/poster.jpg',
            'trailer': 'http://example.com/trailer.mp4',
            'start_date': '2024-03-25',
            'status': 'coming_up',
            'ranking': 0,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(Movie.objects.get().name, 'Test Movie')

    def test_list_movies(self):
        Movie.objects.create(name='Test Movie', protagonists='John Doe', poster='http://example.com/poster.jpg', trailer='http://example.com/trailer.mp4', start_date='2024-03-25', status='coming_up', ranking=0)
        url = reverse('movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
