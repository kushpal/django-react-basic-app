import jwt
import json
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework import generics, status
from rest_framework.response import Response
from Tasks.models import JsonFileUpload
from . import serializers

class UserLogin(generics.CreateAPIView):

    permission_classes = []
    serializer_class = serializers.UserSerializer

    def create(self, request, *args, **kwargs):

        username = request.data.get("username")
        password = request.data.get("password")
        if username is None and password is None:
            response = {
                "status_code": status.HTTP_401_UNAUTHORIZED,
                "message": " Wrong User name and password",
            }
        else:
            if User.objects.filter(username=username, is_active=True).exists():
                user = authenticate(request=self.request, username=username, password=password)
                if user:
                    try:
                        login(self.request,user)
                        payload = jwt_payload_handler(user)
                        token = jwt.encode(payload, settings.SECRET_KEY)
                        response ={
                            "status_code": 200,
                            "message": "success",
                            "result" :{

                                "username": user.username,
                                "email": user.email,
                                "first_name": user.first_name,
                                "last_name": user.last_name,
                                "token" : token,
                                "is_superuser": user.is_superuser
                            }
                        }
                    except Exception as e:
                        response = {
                            "status_code": status.HTTP_401_UNAUTHORIZED,
                            "message": "Your account is deactivated",
                        }
                else:
                    response = {
                        "status_code": status.HTTP_401_UNAUTHORIZED,
                        "message": " Wrong User name and password",
                    }

            else:
                response = {
                    "status_code": status.HTTP_401_UNAUTHORIZED,
                    "message": "Your account is deactivated",
                }




        if not User.objects.filter(username=username).exists():
            response = {
                "status_code": status.HTTP_401_UNAUTHORIZED,
                "message": "Invalid credentials",
            }

        return Response(response)

class JsonFile(generics.ListCreateAPIView):
    #permission_classes = []
    serializer_class = serializers.JsonFileUploadSerializer

    def create(self, request, *args, **kwargs):

        file = self.request.FILES.get("file")
        user = self.request.user
        try:
            data = file.read()
            JsonFileUpload.objects.create(data=json.loads(data),created_by=user)
            response = {
                "status_code": 200,
                "message": "success",
                "result":[]
            }
        except Exception as e:
            response = {
                "status_code": 400,
                "message": "File is not uploaded: "+str(e),
            }

        return Response(response)

    def list(self,request,*args, **kwargs):
        try:
            query_set = JsonFileUpload.objects.all()
            serializer = self.get_serializer(query_set, many=True)


            response = {
                "status_code": 200,
                "message": "success",
                "result": serializer.data
            }

        except Exception as e:
            response = {
                "status_code": 400,
                "message": "Error in file: " + str(e),
            }
        return Response(response)

