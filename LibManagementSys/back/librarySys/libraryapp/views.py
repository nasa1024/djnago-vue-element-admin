from django.shortcuts import render
from rest_framework import viewsets,mixins
from rest_framework import permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_jwt.views import ObtainJSONWebToken
from libraryapp.ser import MyTokenObtainPairSerializer
from rest_framework_simplejwt import authentication
from django.http import JsonResponse
import datetime
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


def get_user_info(request):
    User = get_user_model()
    if request.method == 'GET':
        # print(dir(request))
        # 获取请求参数token的值
        token = request.headers.get('AUTHORIZATION')
        token_msg = authentication.JWTAuthentication().get_validated_token(token)
        user_object = authentication.JWTAuthentication().get_user(token_msg)

        data = {"username": user_object.username,
                "first_name": user_object.first_name,
                "last_name": user_object.last_name,
                #  "avatar":user_object.avatar,
                #  "groups":user_object.groups,
                "roles": [user_object.usertype],
                #  "introduction":user_object.introduction
                }
        re_data = {"data": data,
                   "code": 20000,
                   "message": "success"
                   }
        return JsonResponse(re_data)

