from django.contrib.auth.models import User
from rest_framework import serializers
from Tasks.models import JsonFileUpload

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

class JsonFileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = JsonFileUpload
        fields = "__all__"
        
