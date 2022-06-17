
from django.db import models

from PIL import Image
from django.contrib.auth.models import User



class RecipeModel(models.Model):
    diff_list = (("Easy","Easy"),("Medium","Medium"),("Hard","Hard"))

    name = models.CharField(max_length=50)
    name_in_arabic= models.CharField(max_length=50,default='')

    imageURL = models.ImageField(upload_to='recipes', null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2,null=True)
    type = models.CharField(max_length=100,null=True)
    type_in_arabic = models.CharField(max_length=100,null=True)
    calories = models.IntegerField(null=True)

    video = models.CharField(max_length=500, null=True)

    video_in_arabic = models.CharField(max_length=500, null=True)

    ingridents = models.TextField(default="")

    diff = models.CharField(max_length=10, choices=diff_list, default="Easy")

    ingridents_in_arabic = models.TextField(default="")
    
    time_taken = models.TimeField(null=True)
    
    directions = models.TextField(default="")
    
    directions_in_arabic = models.TextField(default="")


    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name




class RecipesTypes(models.Model):
    type = models.CharField(max_length=100,null=True)
    type_in_arabic = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.type

        
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


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='user',default='default.png')

    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300 :
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


