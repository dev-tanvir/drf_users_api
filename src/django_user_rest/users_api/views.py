from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloAPIView(APIView):
    """ A basic API view class for testing APIView structure."""

    def get(self, request, format=None):
        """ Returns a list of APIView features. """

        apiview_features = [
            'Uses HTTP methods as funtions(get, post, put, patch, delete)',
            'It is similar to traditional django views',
            'Gives you most control over application logic',
            'Is mapped manually to urls'
        ]

    return Response({'message':'Hello! ', 'apiview_features': apiview_features})
