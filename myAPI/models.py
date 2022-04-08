from django.db import models

# Create your models here.
class vehicles(models.Model):
    name = models.CharField(max_length=60)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.name