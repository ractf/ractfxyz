from django.db import models


class Link(models.Model):
    key = models.CharField(max_length=50, blank=False, unique=True)
    link = models.CharField(max_length=2048, blank=False)
    clicks = models.IntegerField(default=0)
