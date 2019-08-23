from django.shortcuts import render, redirect
from .models import Movie
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request, 'movies/index.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    title = request.POST.get('title')
    title_en = request.POST.get('title_en')
    audience = request.POST.get('audience')
    open_date = request.POST.get('open_date')
    genre = request.POST.get('genre')
    watch_grade=request.POST.get('watch_grade')
    score=request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    Movies = Movie.objects.create(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, watch_grade=watch_grade,score=score, poster_url=poster_url, description=description)
    context = {
        'Movie':  Movies
    }
    return render(request, 'movies/create.html', context)

def detail(request, Movie_pk):
    Movies = Movie.objects.get(pk=Movie_pk)
    context = {
        'Movie': Movies
    }
    return render(request, 'movies/detail.html', context)

def delete(request, Movie_pk):
    Movies = Movie.objects.get(pk=Movie_pk)
    Movies.delete()
    return redirect('/movies/')

def update(request, Movie_pk):
    Movies = Movie.objects.get(pk=Movie_pk)
    context = {
        'Movie':Movies,
    }
    return render(request, 'movies/update.html', context)

def upd(request, Movie_pk):
    title = request.POST.get('title')
    title_en = request.POST.get('title_en')
    audience = request.POST.get('audience')
    open_date = request.POST.get('open_date')
    genre = request.POST.get('genre')
    watch_grade=request.POST.get('watch_grade')
    score=request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    Movies = Movie.objects.get(pk=Movie_pk)
    Movies.title = title    
    Movies.title_en = title_en   
    Movies.audience = audience 
    Movies.open_date = open_date 
    Movies.genre = genre    
    Movies.watch_grade= watch_grade
    Movies.score= score     
    Movies.poster_url = poster_url
    Movies.description = description
    Movies.save()
    return redirect('/movies/')