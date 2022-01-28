from django.db import models

class RecipeModel(models.Model):
    name = models.CharField(max_length=50)
    imageURL = models.ImageField(upload_to='recipes', null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    video = models.CharField(max_length=500, null=True)
    ingridents = models.TextField(default="")
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class BreakfastModel(models.Model):
    name = models.CharField(max_length=100)
    imageURL = models.ImageField(upload_to='breakfast', null=True)


    def __str__(self):
        return self.name

class LunchModel(models.Model):
    name = models.CharField(max_length=100)
    imageURL = models.ImageField(upload_to='lunch', null=True)


    def __str__(self):
        return self.name

class DinnerModel(models.Model):
    name = models.CharField(max_length=100)
    imageURL = models.ImageField(upload_to='dinner', null=True)


    def __str__(self):
        return self.name

class SnacksModel(models.Model):
    name = models.CharField(max_length=100)
    imageURL = models.ImageField(upload_to='snacks', null=True)


    def __str__(self):
        return self.name



 