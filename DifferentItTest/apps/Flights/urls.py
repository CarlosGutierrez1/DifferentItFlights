from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *
from apps.Flights.views import FlightViewSet

# Router base Viewset 
router = DefaultRouter()
router.register(r'flights', FlightViewSet, basename='flights')

# Custom url paths
urlpatterns = [
    
    path('', DefaultURIAPIView.as_view()),
    path('', include(router.urls)),
    path('flights/departure/<str:departureIata>/', FlightListByDeparture.as_view()),
    path('flights/arrival/<str:arrivalIata>/', FlightListByArrival.as_view()),
    path('flights/departure/<str:departureIata>/arrival/<str:arrivalIata>/', FlightListByDepartureAndArrival.as_view()),
    path('flights/status/<str:status>', FlightListByStatus.as_view()),

]

