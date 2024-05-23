from django.core.management.base import BaseCommand
from .models import Movie


class Command(BaseCommand):
    help = 'Populate mock movies data'

    def handle(self, *args, **kwargs):
        mock_movies = [
            {'title': 'Inception', 'director': 'Christopher Nolan', 'year': 2010},
            {'title': 'The Shawshank Redemption', 'director': 'Frank Darabont', 'year': 1994},
            {'title': 'The Godfather', 'director': 'Francis Ford Coppola', 'year': 1972},
            {'title': 'Pulp Fiction', 'director': 'Quentin Tarantino', 'year': 1994},
            {'title': 'The Dark Knight', 'director': 'Christopher Nolan', 'year': 2008},
            {'title': 'Forrest Gump', 'director': 'Robert Zemeckis', 'year': 1994},
            {'title': 'The Matrix', 'director': 'Lana Wachowski, Lilly Wachowski', 'year': 1999},
            {'title': 'Fight Club', 'director': 'David Fincher', 'year': 1999},
            {'title': "Schindler's List", 'director': 'Steven Spielberg', 'year': 1993},
            {'title': 'The Lord of the Rings: The Fellowship of the Ring', 'director': 'Peter Jackson', 'year': 2001},
            {'title': 'The Lord of the Rings: The Two Towers', 'director': 'Peter Jackson', 'year': 2002},
            {'title': 'The Lord of the Rings: The Return of the King', 'director': 'Peter Jackson', 'year': 2003},
            {'title': 'The Godfather: Part II', 'director': 'Francis Ford Coppola', 'year': 1974},
            {'title': 'The Dark Knight Rises', 'director': 'Christopher Nolan', 'year': 2012},
            {'title': 'The Silence of the Lambs', 'director': 'Jonathan Demme', 'year': 1991},
            {'title': 'Goodfellas', 'director': 'Martin Scorsese', 'year': 1990},
            {'title': 'Se7en', 'director': 'David Fincher', 'year': 1995},
            {'title': 'The Usual Suspects', 'director': 'Bryan Singer', 'year': 1995},
            {'title': 'Saving Private Ryan', 'director': 'Steven Spielberg', 'year': 1998},
            {'title': 'The Green Mile', 'director': 'Frank Darabont', 'year': 1999}
            # Add more mock movies as needed
        ]
        for movie_data in mock_movies:
            Movie.objects.create(**movie_data)
        self.stdout.write(self.style.SUCCESS('Mock movies created successfully.'))
