from django.db import models

class Release(models.Model):
    """ release year data """
    year = models.CharField(max_length=100)

    class Meta:
        app_label = 'catalog'

    def __str__ (self):
        return f'{self.year}'