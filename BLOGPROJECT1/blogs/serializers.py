from rest_framework import serializers
from .models import blogs
from django.contrib.auth.models import User

class blogsSerializers(serializers.ModelSerializer):
    class Meta:
        model =blogs
        fields = "__all__"

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializers(serializers.Serializer):
    username=serializers.CharField(max_length=50)
    password= serializers.CharField(max_length=50)
    def validate(self,data):
        return data
