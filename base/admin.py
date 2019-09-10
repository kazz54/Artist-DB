from django.contrib import admin

from base.models import Artists, Genre, Albums 
#from base.models import Genre, Track
# Register your models here.

     
class ArtistsAdmin(admin.ModelAdmin):
     pass
	 
class GenreAdmin(admin.ModelAdmin):
     pass

class AlbumsAdmin(admin.ModelAdmin):
     pass	 

admin.site.register(Artists, ArtistsAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Albums, AlbumsAdmin)