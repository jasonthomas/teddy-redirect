from django.db import models

class Url(models.Model):
    short = models.CharField(max_length=10, primary_key=True, db_index=True)
    url = models.CharField(max_length=1000)
    title = models.CharField(max_length=3000, blank=True, null=True)
    source = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
