from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# htpp://127.0.0.1:8000 ==django server 

## uygulama_1

def index_1(requests):
    return HttpResponse('<h1> hello from pages/views via apps </h1>')

##bunu aynı klosör içindeki (pages/urls.py )  urls.py da urlpatterns kısmında eklememiz lazım.


## uygulama_2
def index_2(request):
    return render(request,'pages/index.html') #biz templates klosörünün dizinini catalog/settings.py 
    #içinde zaten tanımladık şimdi kalan kısmını verdik.

def about(request):
    return render(request,'pages/about.html')

## UYGULAMA_3
def index_sayfasi(request):
    return render(request,'pages/indexsayfasi.html')

def about_sayfasi(request):
    return render(request,'pages/aboutsayfasi.html')

## UYGULAMA_4
def layout_index(request):
    return render(request,'pages/layout_index.html')

def layout_about(request):
    return render(request, 'pages/layout_about.html')