from django.conf.urls import url
from django.urls import path
from Tasks.views import UserLogin,JsonFile

urlpatterns = [
    path("login/", UserLogin.as_view()),
    path("json-file/",JsonFile.as_view())
]