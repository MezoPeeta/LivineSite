from django.db import models

class RecipeModel(models.Model):
    name = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
 