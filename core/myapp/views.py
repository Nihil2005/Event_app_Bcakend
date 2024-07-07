from rest_framework import generics
from .models import Event
from .serializer import EventSerializer

class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
