from api.models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class RecipeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = RecipeModel
        fields = ['id','name', 'imageURL','rating','video','ingridents']


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
