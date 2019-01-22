from django.db import models

# Create your models here.

class Link(models.Model):

    label = models.CharField(max_length=100)
    link = models.CharField(max_length=250)
    criado = models.DateField(auto_now_add=True)
    alterado = models.DateField(auto_now=True)

    def __str__(self):
        return self.label

    class Meta:
        ordering = ['label']