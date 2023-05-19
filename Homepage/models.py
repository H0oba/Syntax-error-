from django.db import models

class Card(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    order = models.PositiveIntegerField(default=0)
