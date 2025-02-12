from django.db import models
from django.urls import reverse

class Inscription(models.Model):
    name = models.CharField(max_length=100)
    event = models.CharField(max_length=200)
    date = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('inscription_detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.name} - {self.event}"