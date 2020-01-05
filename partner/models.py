from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=256)
    agent = models.CharField(max_length=256, blank=True)
    industry = models.CharField(max_length=128)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name
