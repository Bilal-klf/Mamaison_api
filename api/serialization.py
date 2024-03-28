from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from api.models import users
from django.contrib.auth.hashers import make_password
from api.models import house_data

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = users.objects.create(**validated_data)
        return user

    class Meta:
        model = users
        fields = ('name', 'email', 'password', 'phone_number', 'id')
        validators = [
            UniqueTogetherValidator(
                queryset=users.objects.all(),
                fields=['name', 'email']
            )
        ]


class HouseDataSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        data = house_data.objects.create(**validated_data)
        return data

    class Meta:
        model = house_data
        fields = ('temperature', 'humidity', 'windows','id')
       
