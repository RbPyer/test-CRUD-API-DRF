from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import *

from microservice.serializers import *


# Create your views here.

class MicroserviceAPIList(generics.ListCreateAPIView):
    queryset = Microservice.objects.all()
    serializer_class = MicroserviceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class MicroserviceAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Microservice.objects.all()
    serializer_class = MicroserviceSerializer
    permission_classes = (IsAuthenticated,)


class MicroserviceAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Microservice.objects.all()
    serializer_class = MicroserviceSerializer
    permission_classes = (IsAdminOrReadOnly,)
