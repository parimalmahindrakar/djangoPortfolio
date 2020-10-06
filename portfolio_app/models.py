from django.db import models

# Create your models here.

class MyViews(models.Model):
    email = models.EmailField(max_length=200)
    view = models.TextField()

    def __str__(self):
        return self.email