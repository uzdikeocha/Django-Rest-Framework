from django.shortcuts import render
from rest_framework import generics
from .models import Song, Artiste
from .serializers import SongSerializer, ArtisteSerializer

# Create your song view here.
class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

# create your artiste view here
class ArtisteList(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class =ArtisteSerializer

class ArtisteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Artiste.objects.all()
    serializer_class = ArtisteSerializer    