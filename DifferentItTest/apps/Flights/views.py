from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import viewsets

from .serializers.Flight import FlightModelSerializer
from .models import Flight


# Return all URLs for the API
class DefaultURIAPIView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get(self, request):
        fullURI = request.build_absolute_uri()
        data = {
            'URI': [
                {'url': '{}flights/'.format(fullURI), 'method': 'GET', 'description': 'List all flights'},
                {'url': '{}flights/'.format(fullURI), 'method': 'POST', 'description': 'Create a new flight'},
                {'url': '{}flights/<int:pk>/'.format(fullURI), 'method': 'GET', 'description': 'Get a flight by ID'},
                {'url': '{}flights/<int:pk>/'.format(fullURI), 'method': 'PUT', 'description': 'Update a flight'},
                {'url': '{}flights/<int:pk>/'.format(fullURI), 'method': 'DELETE', 'description': 'Delete a flight'},
                {'url': '{}flights/departure/<str:departureIata>/'.format(fullURI), 'method': 'GET', 'description': 'Get a flight by departure IATA'},
                {'url': '{}flights/arrival/<str:arrivalIata>/'.format(fullURI), 'method': 'GET', 'description': 'Get a flight by arrival IATA'},
                {'url': '{}flights/departure/<str:departureIata>/arrival/<str:arrivalIata>/'.format(fullURI), 'method': 'GET', 'description': 'Get a flight by departure IATA and arrival IATA'},
                {'url': '{}flights/status/<str:status>/'.format(fullURI), 'method': 'GET', 'description': 'Get a flight by status'},
            ]
        }
        return Response(data, status=status.HTTP_200_OK)

# Basic CRUD operations for the Flight model
class FlightViewSet(viewsets.ViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = (AllowAny, )

    def list(self, request):
        queryset = Flight.objects.all()
        serializer = FlightModelSerializer(queryset, many=True)
        data = {
            'URI': request.build_absolute_uri(),
            'flights': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    def create(self, request):
        serializer = FlightModelSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, pk=None):
        try:
            queryset = Flight.objects.get(pk=pk)
        except Flight.DoesNotExist:
            raise Http404
        serializer = FlightModelSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def update(self, request, pk=None):
        try:
            queryset = Flight.objects.get(pk=pk)
        except Flight.DoesNotExist:
            raise Http404
        serializer = FlightModelSerializer(queryset, data=request.data)
        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        try:
            queryset = Flight.objects.get(pk=pk)
        except Flight.DoesNotExist:
            raise Http404
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Return all flights by departure IATA
class FlightListByDeparture(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = (AllowAny, )
    def get(self, request, departureIata):
        flights = Flight.objects.filter(departureIata=departureIata)
        serializer = FlightModelSerializer(flights, many=True)
        return Response(serializer.data)

# Return all flights by arrival IATA
class FlightListByArrival(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = (AllowAny, )
    def get(self, request, arrivalIata):
        flights = Flight.objects.filter(arrivalIata=arrivalIata)
        serializer = FlightModelSerializer(flights, many=True)
        return Response(serializer.data)

# Return all flights by departure IATA and arrival IATA
class FlightListByDepartureAndArrival(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = (AllowAny, )
    def get(self, request, departureIata, arrivalIata):
        flights = Flight.objects.filter(departureIata=departureIata, arrivalIata=arrivalIata)
        serializer = FlightModelSerializer(flights, many=True)
        return Response(serializer.data)

# Return all flights by status
class FlightListByStatus(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = (AllowAny, )
    def get(self, request, status):
        flights = Flight.objects.filter(status=status)
        serializer = FlightModelSerializer(flights, many=True)
        return Response(serializer.data)

