from django.db import models

class Player(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=60)

    def __str__(self):
        return self.email
