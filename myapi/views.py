from django.shortcuts import render
from myapi.serializers import HeroSerializer
from myapi.models import Hero
from rest_framework import viewsets

# Create your views here.

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
     