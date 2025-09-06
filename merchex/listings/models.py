from django.db import models

class Band(models.Model):
    
    title = models.fields.CharField(max_length=100)
