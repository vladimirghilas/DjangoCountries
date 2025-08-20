from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)
    languages = models.JSONField(default=list)

    def __str__(self):
        return self.name


