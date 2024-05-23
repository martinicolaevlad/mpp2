from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from .models import Movie, CastMember


class MovieCRUDTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Movie.objects.create(title="Movie", director="Director", year=2000)


    def test_create_movie(self):
        url = '/api/movies/'
        data = {'title': 'New Movie', 'director': 'New Director', 'year': 2022}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_movie_with_invalid_title(self):
        url = '/api/movies/'
        # Invalid data: Empty title
        data = {'title': '', 'director': 'New Director', 'year': 2022}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_movie_with_invalid_director(self):
        url = '/api/movies/'
        # Invalid data: Empty director
        data = {'title': 'Invalid Movie', 'director': '', 'year': 2022}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_movie_with_invalid_year(self):
        url = '/api/movies/'
        # Invalid data: Year out of range
        data = {'title': 'Invalid Movie', 'director': 'New Director', 'year': 3000}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_movies(self):
        url = '/api/movies/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_movie(self):
        movie_id = Movie.objects.first().id
        url = f'/api/movies/{movie_id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_movie(self):
        movie_id = Movie.objects.first().id
        url = f'/api/movies/{movie_id}/'
        data = {'title': 'Updated Movie', 'director': 'Director', 'year': 2022}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Movie.objects.get(id=movie_id).title, 'Updated Movie')

    def test_update_movie_with_invalid_title(self):
        movie_id = Movie.objects.first().id
        url = f'/api/movies/{movie_id}/'
        data = {'title': '', 'director': 'Director', 'year': 2022}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_movie_with_invalid_director(self):
        movie_id = Movie.objects.first().id
        url = f'/api/movies/{movie_id}/'
        data = {'title': 'Title', 'director': '', 'year': 2022}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_movie_with_invalid_year(self):
        movie_id = Movie.objects.first().id
        url = f'/api/movies/{movie_id}/'
        data = {'title': 'Title', 'director': 'Director', 'year': 3000}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_movie(self):
        movie_id = Movie.objects.first().id
        url = f'/api/movies/{movie_id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(id=movie_id).exists())


