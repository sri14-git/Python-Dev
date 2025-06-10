from django.db import models

# Create your models here.

class form(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
