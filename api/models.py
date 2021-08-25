from django.db import models

class RecipeModel(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    