from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
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
        

    def put(self, request, pk=None):
        """ Handles update of an object with 'pk' as database id."""

        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """ Handles update of only provided fields of an object with 'pk' as database id."""

        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """ Handles deletion of an object with 'pk' as database id."""

        return Response({'method':'DELETE'})


class HelloViewsets(viewsets.ViewSet):
    """ Testing DRF viewsets class."""

    def list(self, request):
        """ Returns a list of Viewsets features. """

        viewset_features = [
            'Uses actions as functions(list, retrieve, update, partial update, delete.)'
            'Automatically maps urls to viewsets using Routers',
            'Provides more funtionality with less code',
            'Faster database CRUD operations',
        ]

        return Response({'message':'Viewsets Features', 'viewset_features': viewset_features})

    def create(self, request):
        """ Creates a message with the name that was given./ POST method"""

        serializer = serializers.TestSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ Handles getting an object with 'pk' as database id."""

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """ Handles update of an object with 'pk' as database id."""

        return Response({'method':'PUT'})