from rest_framework import serializers
from apps.Flights.models import Flight


class FlightModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'