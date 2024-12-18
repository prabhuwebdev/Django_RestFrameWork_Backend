from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=300,allow_null=False,required=True)
    email=serializers.EmailField()
    password=serializers.CharField(max_length=300,allow_null=False,required=True)

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username=data['username']):
                raise serializers.ValidationError("The username is already exits")

        if data['email']:
            if User.objects.filter(email=data['email']):
                raise serializers.ValidationError("The email is already taken")

        return data

    def create(self, validated_data):
        user=User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data


class LoginSerializers(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    # def create(self, validated_data):
    #     user=User.objects.create(username=validated_data['username'])
    #     user.set_password(validated_data['password'])
    #     return validated_data

class Colorserializer(serializers.ModelSerializer):
    class Meta:
        model=Color
        fields=["color_name"]
class personserializer(serializers.ModelSerializer):
    # color = Colorserializer()
    country=serializers.SerializerMethodField()
    class Meta:
        model=Person
        fields="__all__"

    def get_country(self,obj):
        return "india"


    def validate(self, data):
        special_characters = "!@#$%^&*()_-+={}[]|\\:;\"'<>,.?/~`"
        if any(c in special_characters for c in data['Name']):
            raise serializers.ValidationError("Name should not contain special character")
        if data["Age"]<12:
            raise serializers.ValidationError("Age should be above 15")
        return data

