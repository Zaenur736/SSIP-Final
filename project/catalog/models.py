from django.db import models


class Release(models.Model):
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.year


class Song(models.Model):
    title = models.CharField(max_length=200)
    songwriter = models.ForeignKey('SongWriter', on_delete=models.SET_NULL, null=True)
    release = models.ManyToManyField(Release)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class SongWriter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
