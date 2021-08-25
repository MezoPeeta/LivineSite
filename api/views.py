from api.models import RecipeModel
from api.serializers import RecipeSerializer
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

def index(request):
    return render(request, 'api/index.html')

@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        recipe = RecipeModel.objects.all()
        serializer = RecipeSerializer(recipe, many=True)
        return Response(serializer.data)

