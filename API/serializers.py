from rest_framework import serializers
from .models import Singer, Song

# Model Serializer


class SingerSerializer(serializers.ModelSerializer):

    # It creates Hyperlink of the relation
    # song = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='song-detail')

    # Serializer Relation
    song = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']
