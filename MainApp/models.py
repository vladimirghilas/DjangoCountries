from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    languages = models.ManyToManyField(Language, related_name='countries')

    def __str__(self):
        return self.name


