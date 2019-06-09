from rest_framework import serializers

class TestSerializer(serializers.Serializer):
    """ Testing rest framework serializers. Serializes a name field for tesing APIView."""

    name = serializers.CharField(max_length=10)