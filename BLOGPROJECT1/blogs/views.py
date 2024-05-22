

from . import models
from . import serializers
from .models import blogs
from .serializers import blogsSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import UserSerializers,LoginSerializers,RegisterSerializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate , login
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class blogsViewSet(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        blog = blogs.objects.all()
        serializer = blogsSerializers(blog, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = serializers.blogsSerializers(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id=None):
        try:
            items = blogs.objects.get(id=id)
            serializer = blogsSerializers(items, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("success",status= 200)
            else:
               return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except blogs.DoesNotExist:
            return Response({"status": "error", "data": "blogs not found"}, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, id=None):
        try:
            item =blogs.objects.get(id=id)
            print(item)
            item.delete()
            return Response({"status": "success", "data": "item deleted"})
        except Exception as e:
            print(f"Error: {e}")
            return Response({"status": "error", "data": "AN ERROR OCCURRED"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)




    #user registeration & login
class RegisterViewSet(APIView):
    def post(self, request):
        serializer = RegisterSerializers(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            print (f"User{User.username} registered successfully!")
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class LoginViewSet(APIView):
    def post(self, request):
        serializer = LoginSerializers(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)

                refresh = RefreshToken.for_user(user)
                print(f"User{username}login successfully!")
                return Response({"status": "success",
                                 "data":{
                                     "user":UserSerializers(user).data,
                                     "access_token": str(refresh.access_token),
                                     "refresh_token": str(refresh)
                                 }
                                 }, status=status.HTTP_200_OK)
            return Response({"status": "error", "data": "invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




