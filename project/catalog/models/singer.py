from django.db import models

class Singer(models.Model) :
    """ Singer Data """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        app_label = 'catalog'

    def __str__ (self):
        return f'{self.first_name} {self.last_name}'