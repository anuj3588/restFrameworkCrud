from rest_framework import serializers
from .models import student, studentClass, Track, Album


class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentClass
        fields = '__all__'
        depth = 1


class StudentSerializer(serializers.ModelSerializer):
    class_details = StudentClassSerializer(read_only=True, many=True)
    
    class Meta:
        model = student
        fields = '__all__'



# from docs
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'
    
    def setup_eager_loading(cls, queryset):
        """ Perform necessary eager loading of data. """
        queryset = Track.prefetch_related('album')
        return queryset

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']

    # def create(self, validated_data):
    #     tracks_data = validated_data.pop('tracks')
    #     album = Album.objects.create(**validated_data)
    #     for track_data in tracks_data:
    #         Track.objects.create(album=album, **track_data)
    #     return album
 

