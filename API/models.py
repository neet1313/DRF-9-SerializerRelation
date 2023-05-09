from django.db import models


# Create your models here.


class Singer(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.name} ({self.gender})'


class Song(models.Model):
    title = models.CharField(max_length=50)
    duration = models.IntegerField()
    singer = models.ForeignKey(
        Singer, on_delete=models.CASCADE, related_name='song')

    def __str__(self):
        return self.title
