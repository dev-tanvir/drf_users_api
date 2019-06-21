from rest_framework import serializers
from . import models


class TestSerializer(serializers.Serializer):
    """ Testing rest framework serializers. Serializes a name field for tesing APIView."""

    name = serializers.CharField(max_length=10)

# The main API serializers
class UserProfileSerializer(serializers.ModelSerializer):
    """ A serializer for user profile objects. """

    class Meta:
        model = models.UserProfiles     #   this is to define the model that 
                                        #   will be used by our serializer
                                        #  
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """  Creates and returns a user object. """

        user = models.UserProfiles(
            email = validated_data['email'],
            name = validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileStatusSerializer(serializers.ModelSerializer):
    """ A serializer for user profile objects. """
    
    class Meta:
        model = models.ProfileStatus
        fields = ('id', 'user_profile', 'status_text', 'creation_date')
        extra_kwargs = {'user_profile': {'read_only': True}}

