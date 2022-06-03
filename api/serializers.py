from api.models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class RecipeSerializer(serializers.ModelSerializer):
    ingridents = serializers.SerializerMethodField(source="ingridents")
    ingridents_in_arabic = serializers.SerializerMethodField(source="ingridents_in_arabic")
    
    directions = serializers.SerializerMethodField(source="directions")

    directions_in_arabic = serializers.SerializerMethodField(source="directions_in_arabic")

    difficulty = serializers.CharField(source='difficulty.name')


    def get_ingridents(self, instance):
        ig = instance.ingridents.splitlines()
        x = [x for x in ig if x]
        return x

    def get_ingridents_in_arabic(self, instance):
        ig_a = instance.ingridents_in_arabic.splitlines()
        x = [x for x in ig_a if x]
        return x
    
    def get_directions(self, instance):
        dr = instance.directions.splitlines()
        x = [x for x in dr if x]
        return x

    def get_directions_in_arabic(self, instance):
        dr_a = instance.directions_in_arabic.splitlines()
        x = [x for x in dr_a if x]
        return x


    
    class Meta: 
        model = RecipeModel
        fields = '__all__' 


class RecipeTypesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = RecipesTypes
        fields = '__all__' 

class BreakfastSerializer(serializers.ModelSerializer):
    class Meta: 
        model = BreakfastModel
        fields = ['id','name', 'imageURL']

class LunchSerializer(serializers.ModelSerializer):
    class Meta: 
        model = LunchModel
        fields = ['id','name', 'imageURL']

class DinnerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = DinnerModel
        fields = ['id','name', 'imageURL']

class SnacksSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SnacksModel
        fields = ['id','name', 'imageURL']



# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
