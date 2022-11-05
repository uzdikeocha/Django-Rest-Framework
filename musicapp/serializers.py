from rest_framework import serializers
from .models import Song, Artiste

# create your serializers here
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = (
            "id",
            "title",
            "date_released",
            "likes",
            "artist_id",  
        )
       
class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:  
        model = Artiste    
        fields = (
            "id",
            "first_name",
            "last_name",
            "age",
        )