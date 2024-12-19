from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from.models import *
from .serializers import personserializer,LoginSerializers,Colorserializer,RegisterSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework import status



class RegisterApi(APIView):
    def post(self,request):
        data=request.data
        print((request.data))
        serializer=RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data":serializer.data,
                "Result":"user Created"

            })
        return Response(serializer.errors)


class LoginApi(APIView):
    def post(self,request):
        data=request.data
        serializer=LoginSerializers(data=data)
        if not serializer.is_valid():
            return Response({
                "Result": "not valid"

            },status=status.HTTP_400_BAD_REQUEST)
        print(serializer.data)
        user = authenticate(username=serializer.data['username'],password=serializer.data['password'])
        if not user:
            return Response({
                "user":"invalid credentials"
            },status=status.HTTP_404_NOT_FOUND)
        token,_=Token.objects.get_or_create(user=user)
        print(token.key)
        return Response({
            "message":"successfully login",
            "token":token.key
        })




class PersonApi(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self,request):
        print(request.data)
        objs = Person.objects.all()
        # objs=Person.objects.filter(color__isnull=False)
        serializer = personserializer(objs, many=True)
        return Response(serializer.data)


    def post(self,request):
        data = request.data
        serializers = personserializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)


    def patch(self,request):
        data = request.data
        objs = Person.objects.get(id=data['id'])
        serializers = personserializer(objs, data=data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)


    def delete(self,request):
        data = request.data
        objs = Person.objects.get(id=data['id'])
        objs.delete()
        return Response("data Deleted")

@api_view(["POST"])
def login(request):
    data=request.data
    serializer=LoginSerializers(data=data)
    if serializer.is_valid():
        # data=serializer._validated_data
        print(serializer.data)
        return Response("successfully registered")
    return Response(serializer.errors)

@api_view(["GET","POST","PUT","PATCH","DELETE"])
def person(request):
    if request.method=="GET":
        objs=Person.objects.all()
        # objs=Person.objects.filter(color__isnull=False)
        serializer=personserializer(objs,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        data=request.data
        serializers=personserializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

    elif request.method=="PATCH":
        data = request.data
        objs=Person.objects.get(id=data['id'])
        serializers = personserializer(objs,data=data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

    else:
        data=request.data
        objs=Person.objects.get(id=data['id'])
        objs.delete()
        return Response("data Deleted")


# class PeopleViewSet(viewsets.ModelViewSet):
#     queryset = Person.objects.all()
#     serializer_class=personserializer


