from django.db import models

class Genre(models.Model):
    """ genre data """
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'catalog'

    def __str__ (self):
        return self.name