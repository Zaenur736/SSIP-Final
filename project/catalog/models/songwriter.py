from django.db import models

class SongWriter(models.Model):
    """ song writer data """
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        app_label = 'catalog'

    def __str__ (self):
        return f'{self.name}'