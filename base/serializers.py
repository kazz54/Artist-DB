from rest_framework import serializers
from base.models import Artists, Albums


class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = ['id', 'name', 'cover', 'bio', 'albums']
        depth = 2
class AlbumsSerializer(serializers.ModelSerializer):

    

    class Meta:

        model = Albums
        fields = ('albumId', 'title', 'year', 'cover', 'genre')



			