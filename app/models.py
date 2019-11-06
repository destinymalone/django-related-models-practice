from django.db import models


class Album(models.Model):
    title = models.TextField()
    artist_name = models.TextField()

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.TextField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    seconds = models.IntegerField("M:SS")

    def __str__(self):
        return f"{self.title} at {self.seconds}"

