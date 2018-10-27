from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    emaild = models.URLField(unique = True)

    def __str__(self):
        return self.emaild
