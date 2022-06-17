import email
from api.models import RecipeModel, BreakfastModel
from api.serializers import *
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
from rest_framework import status


def index(request):
    return render(request, 'api/index.html')

@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        recipe = RecipeModel.objects.all()
        serializer = RecipeSerializer(recipe, many=True)
        
        return Response(serializer.data)



@api_view(['GET'])
def recipeDetail(request,pk):
    if request.method == "GET":
        recipe = RecipeModel.objects.get(pk=pk)
        serializer = RecipeSerializer(recipe)
    
        return Response(serializer.data)




@api_view(['GET'])
def recipeTypeDetail(request,type):
    if request.method == "GET":
        recipe = RecipeModel.objects.filter(type=type)
        serializer = RecipeSerializer(recipe,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def recipe_all_types(request):
    if request.method == "GET":
        recipe = RecipesTypes.objects.all()
        serializer = RecipeTypesSerializer(recipe,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def breakfast(request):
    if request.method == 'GET':
        recipe = BreakfastModel.objects.all()
        serializer = BreakfastSerializer(recipe, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def lunch(request):
    if request.method == 'GET':
        recipe = LunchModel.objects.all()
        serializer = LunchSerializer(recipe, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def dinner(request):
    if request.method == 'GET':
        recipe = DinnerModel.objects.all()
        serializer = DinnerSerializer(recipe, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def snacks(request):
    if request.method == 'GET':
        recipe = SnacksModel.objects.all()
        serializer = SnacksSerializer(recipe, many=True)
        return Response(serializer.data)




# Register User
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        print("This Email " + serializer.validated_data['email'])

        emailExist = User.objects.filter(email = email).exists()

        if emailExist:
            return Response(
                {
                'email' : "This email already exists"
            },
            status = status.HTTP_400_BAD_REQUEST
            )
        else:
            user = serializer.save()
            return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
            })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print(user.id)
        try:
            login(request, user)
        except:
            print("Error")

        temp_list=super(LoginAPI, self).post(request, format=None)
        temp_list.data['user_id'] = user.id 
        return Response({"data":temp_list.data})



@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "pristineguava@gmail.com",
        # to:
        [reset_password_token.user.email]
    )


@api_view(['GET'])
def get_users(request,pk):
    if request.method == "GET":
        users = User.objects.get(pk=pk)
        serializer = UserSerializer(users)
        return Response(serializer.data)


@api_view(['POST'])
def user_update(request,pk):
    if request.method == "POST":
        user = User.objects.get(pk=pk)
        
        
        serializer = UserSerializer(instance = user , data = request.data)

        if serializer.is_valid():
            serializer.save()
            
     
        return Response(serializer.data)
