from django.db import models

class Difficulty(models.Model):
    diff = (("Easy","Easy"),("Medium","Medium"),("Hard","Hard"))
    name = models.CharField(choices=diff, max_length=10)

    def __str__(self):
        return self.name

class RecipeModel(models.Model):
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

    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE, null=True)

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



 