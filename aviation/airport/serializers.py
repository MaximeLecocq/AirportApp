from rest_framework import serializers
from .models import Airport

# Serializer for the Airport model
class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport # Specifies the model to be serialized
        fields = ['airport_id', 'airport_name','airport_type','latitude','longitude','elevation','continent','country','municipality']
        # Defines the fields to be included in the serialized representation of Airport objects