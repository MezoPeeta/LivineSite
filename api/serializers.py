from api.models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
import base64
import six
import uuid


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

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension




# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'



# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
