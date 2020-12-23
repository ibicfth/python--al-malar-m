from django.contrib import admin

# Register your models here.
##hangi klasörden modelleri alacaksak dosyayı ekleriz

from .models import Movie  # movie classını modelini ekleriz


class MovieAdmin(admin.ModelAdmin):
    list_display=('id','name','create_date', 'isPublished') 
    list_display_links=('id','name') ## id ve name için link oluşturduk
    list_filter=('create_date',)
    list_editable=('isPublished',) ##onay kutusu ekler
    search_fields=('name','description')
    list_per_page=1 ##sayfada kaçtane listeleme yapmak istediğimizi söyler

admin.site.register(Movie, MovieAdmin) ##modesl dosyasının movie modeli(klası) ile 
## bu dosya içinde kendimizin tanımladığı MovieAdmin klasını database kaydederiz.
