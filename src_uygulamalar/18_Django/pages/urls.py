from django.urls import path
from . import views  # aynı dizindeki dosyayı çağırdığımızdan dizine . dedik

# htpp://127.0.0.1:8000 ==django server  ==>localhost tur
#bu local host catalog/urls.py dan belirlenir .Eğer orada localhosta:htpp://127.0.0.1:8000/degisti
#dersek artık ana sayfa dns i :htpp://127.0.0.1:8000/degisti olur.

urlpatterns= [
    path('index_ac_1',views.index_1, name='index_1'),
    path('index_ac_2',views.index_2,name='index_2'),
    path('about_ac_1',views.about,name='about_1'),
    path('index_sayfasi_ac',views.index_sayfasi,name='index_sayfasi'),
    path('about_sayfasi_ac',views.about_sayfasi,name='about_sayfasi'),
    path('layoutindex_ac',views.layout_index,name='layout_index'),
     path('layoutabout_ac',views.layout_about,name='layout_about')

]

''' burada server ana adres girildiğinde istediğimiz talebin gelmesini istiyorsak
path methodunun ilk parametresine '' verdik eğer htpp://127.0.0.1:8000/index
girdiğimizde gelmesini istiyorsak path parametresinin ilk değerine 'index' vermemiz lazım

yani ilk parametre dizin belirtiriz

2. paramterede ise 1.parametredeki dizinde ne gösterilsin talebmiz ne onu belirtiriz
burda taleb views dosyasının index methodunu taleb ettik

3. paramterede ise bu işleme talebe bi isim verdik '''

