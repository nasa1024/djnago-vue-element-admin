from libraryapp.models import UserProfile
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # print('in MyTokenObtainPairSerializer')
        token = super().get_token(user)
        # Add custom claims
        # token['username'] = user.username
        # token['code'] = 20000
        # print(token)
        # ... 官方示例中上面的部分没有生效
        # print(token)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        re_data = {}
        re_data['data'] = data
        re_data['code'] = 20000
        re_data['message'] = 'success'

        return re_data


