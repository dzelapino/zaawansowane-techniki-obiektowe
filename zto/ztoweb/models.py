from django.db import models

# Create your models here.

class Subscriber(models.Model):

    # Adres email subskrybenta, nie może się powtarzać
    email = models.EmailField(unique=True)
    def __str__(self):
        return "Subscriber: " + self.email

class Hero(models.Model):

    name = models.CharField(max_length=100)
    about = models.TextField()
    color = models.TextField()
    def __str__(self):
        return self.name