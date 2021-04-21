from django.shortcuts import render
from django.contrib.auth.models import User
from ecommerce.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


@api_view(['GET'])
def UserList(request):
    obj_list = User.objects.all()
    serializers = UserSerializer(obj_list, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def UserDetail(request, pk):
    obj = User.objects.get(id=pk)
    serializer = UserSerializer(obj)
    return Response(serializer.data)

@api_view(['POST'])
def UserCreate(request):
    serializer = UserSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = 'Successfully registered a new user.'
        data['email'] = user.email
        data['username'] = user.username
        token = Token.objects.get(user=account).key
        data['token'] = token
    else:
        data = serializer.errors
        

    return Response(data)