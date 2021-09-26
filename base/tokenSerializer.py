from rest_framework import serializers
from .models import userToken

class token_serializer(serializers.ModelSerializer):
    class Meta:
        model = userToken
        fields = ['token']

    def create(self, validated_data):
        return userToken.objects.create(**validated_data)


    