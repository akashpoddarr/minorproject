from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    screen_shot = models.ImageField(upload_to='screenshots/')
    movie_length = models.CharField(max_length=50)
    release_date = models.DateField()
    movie_rate = models.CharField(max_length=100)
    imdb_rating = models.CharField(max_length=100)
    movie_director = models.CharField(max_length=200)
    movie_actor = models.CharField(max_length=1000)
    movie_language = models.CharField(max_length=100)
    movie_size = models.CharField(max_length=100)
    movie_subtitle = models.CharField(max_length=100)
    movie_link = models.TextField(max_length=10000)
    movie_online = models.TextField(max_length=100)
    movie_type = models.CharField(max_length=700)
    movie_subscription = models.CharField(max_length=700)
    movie_category = models.CharField(max_length=100)

