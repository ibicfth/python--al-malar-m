from django.shortcuts import render,get_object_or_404
from .models import Movie
from django.http import Http404

# Create your views here.

def index(request):
    movies=Movie.objects.all()
    context= {
        'movies':movies
    }
    return render(request, 'movies/list.html', context) ##templates e kadar olan dizini vermiştir şimdi
    ##templates aldtındaki movies klasöründeki  index.html yi taleb ettik.

def detail(request, movie_id):
    try:
        movie = Movie.objects.get(pk = movie_id)
    except Movie.DoesNotExist:
        raise Http404('aradığınız kayıt bulunmamaktadır. ')

    ##movie yi direkt 3 parametre olarak veremeyiz. bir obje tanımlayıp key value yapmalıyız.
    context= {
        'movie': movie
    }
    return render(request, 'movies/detail.html',context)

def search(request):
    return render(request, 'movies/search.html')

