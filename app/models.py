from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.TextField()
    email=models.EmailField()
    message=models.TextField()
    def __str__(self):
        return self.name