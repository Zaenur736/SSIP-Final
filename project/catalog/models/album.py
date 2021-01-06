from django.db import models
from catalog.models.release import Release
from catalog.models.singer import Singer

class Album(models.Model):
    """ song album data """
    name = models.CharField(max_length=100)
    year = models.ForeignKey(Release, on_delete=models.SET_NULL, null=True)
    singer = models.ForeignKey(Singer, on_delete=models.SET_NULL, null=True)

    class Meta:
        app_label = 'catalog'

    def __str__ (self):
        return f'{self.name}'