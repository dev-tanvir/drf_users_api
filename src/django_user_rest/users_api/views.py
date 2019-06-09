from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.

class HelloAPIView(APIView):
    """ A basic API view class for testing APIView structure."""

    serializer_class = serializers.TestSerializer   #   This is to tell DRF which serializers we are
                                                    #   using for this APIView.Here, it is HelloAPIView.

    def get(self, request, format=None):
        """ Returns a list of APIView features. """

        apiview_features = [
            'Uses HTTP methods as funtions(get, post, put, patch, delete)',
            'It is similar to traditional django views',
            'Gives you most control over application logic',
            'Is mapped manually to urls'
        ]

        return Response({'message':'Hello! ', 'apiview_features': apiview_features})

    def post(self, request):
        """ Creates a message with the name that was posted."""

        serializer = serializers.TestSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  #   without status, it shows 200 ok
                                                                                    #   even when not valid!!! 
        


