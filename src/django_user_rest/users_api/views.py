from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from . import serializers
from . import models
from . import permissions

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

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """ Handles partial update of an object with 'pk' as database id."""

        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """ Handles deletion of an object with 'pk' as database id."""

        return Response({'http_method':'DELETE'})


#   the main viewswt for our API
class UserProfileViewset(viewsets.ModelViewSet):
    """ Handles creating, reading and updating user profiles. """

    serializer_class = serializers.UserProfileSerializer
    # in ModelViewSet , we know the model as it is already added in UserProfileSerializer
    queryset = models.UserProfiles.objects.all()
    authentication_classes = (TokenAuthentication,)     # the authentication method that will be used
    permission_classes = (permissions.UpdateOwnProfile,)   # the access or permission point of the user
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email','name',)

class LoginViewSet(viewsets.ViewSet):
    """ Checks email and password and returns an auth token."""
    """ By default, DRF has login APIView but we want viewset. So, here
        we, first take an object of ObtainAuthToken APIView class and pass the request 
        to its post() method as we might have done if we had used APIView itself.

        As we are tricking it to use in a ViewSet( why? cause we want to use
        the DefaultRouter() od DRF!!! ), we did the whole process in 
        Viewsets create() method as normal viewsets are designed to do.
    """

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """  Use ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)


