from base.models import Artists
from rest_framework import viewsets
from .serializers import ArtistsSerializer




class ArtistsViewSet(viewsets.ModelViewSet):
    
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializer

     
