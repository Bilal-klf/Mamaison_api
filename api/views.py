from api.models import *
from api.serialization import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAdminUser
from django.contrib.auth.hashers import check_password


class UserRecordView(APIView):
    
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    #permission_classes = [IsAdminUser]


    def post(self, request):
        """content = request.data.get('_content')
        if content:
            content_data = json.loads(content)"""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

class getUserExist(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=400)
        try:
        # Check if a user with the provided email exists
            user = users.objects.get(email=email)
        except user.DoesNotExist:
            return Response({'error': 'User not found'}, status=202)
        if check_password(password, user.password):
            # User authentication successful
            return Response({'message': 'User authenticated successfully'}, status=status.HTTP_200_OK)
        else:
            # Invalid password
            return Response({'error': 'Invalid password'}, status=401)
        ##results = users.objects.all()
        ##serializer = UserSerializer(results, many=True)

class getHouseData(APIView):

    def get(self, request):
        results = house_data.objects.all()
        serialize = HouseDataSerializer(results, many = True)
        return Response(serialize.data)