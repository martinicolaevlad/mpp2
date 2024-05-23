
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Movie
from faker import Faker
import asyncio

faker = Faker()


class MovieConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            await self.send_movie()
            await asyncio.sleep(5)

    async def send_movie(self):
        movie = await self.generate_fake_movie()
        await self.send(text_data=json.dumps({
            'title': movie.title,
            'director': movie.director,
            'year': movie.year
        }))

    @sync_to_async
    def generate_fake_movie(self):
        movie = Movie.objects.create(
            title=faker.sentence(nb_words=5),
            director=faker.name(),
            year=faker.year()
        )
        return movie
