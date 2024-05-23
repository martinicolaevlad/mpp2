from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Movie, CastMember, User
from django.contrib.auth import authenticate

#Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "first_name", "last_name", "username"]

#Serializer to Register User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ['email', 'password']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        return value

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {
            'password':{'write_only': True}
        }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        # user = User.objects.create_user(
        #     email=validated_data['email'],
        #     password=validated_data['password']
        # )
        # return user

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request=self.context.get('request'), username=email, password=password)
        if not user:
            raise serializers.ValidationError('Unable to authenticate with provided credentials', code='authorization')
        data['user'] = user
        return data

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'director', 'year']

    def validate(self, data):
        errors = {}

        title = data.get('title')
        if not title:
            errors['title'] = ['Title field is required.']

        director = data.get('director')
        if not director:
            errors['director'] = ['Director field is required.']

        year = data.get('year')
        if year is None:
            errors['year'] = ['Year field is required.']
        elif year < 1900 or year > 2024:
            errors['year'] = ['Year must be between 1900 and 2024.']

        if errors:
            raise serializers.ValidationError(errors)

        return data



class CastMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastMember
        fields = ['id', 'name', 'movie_id']

    def validate(self, data):
        errors = {}

        name = data.get('name')
        if not name:
            errors['name'] = ['Name field is required.']

        movie_id = data.get('movie_id')
        if not movie_id:
            errors['movie_id'] = ['Movie ID field is required.']

        if errors:
            raise serializers.ValidationError(errors)

        return data
