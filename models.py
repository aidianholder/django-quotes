from django.db import models


class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=250)
    note = models.TextField(blank=True)
    active = models.BooleanField(default=False)