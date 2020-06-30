from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import views
from .models import Movie
#from .forms import MovieForm


# Hay dos formas de crear vistas
#1.- Creando una clase -> Tenemos dos o más métodos HTTP en la misma ruta 
#2.- Creando una funcion -> Solo tenemos un método HTTP en la ruta
def GetMovies(request):
    #vamos a traer todas las peliculas
    #SELECT * FROM movies_movie WHERE  seria la consulta equivalente, pero aqui se usa un ORM
    movies = Movie.objects.all()#queryset (es lo que el ORM retorna)
    print(movies)
    return HttpResponse('Funciona!')#para mostrar un texto en la pantalla y quitar la pantalla amarilla de error

'''
#class CreateMovie(views.View):
    def get(self, request):
        template_name = 'movies/form.html'
        return render(request, template_name)

    def post(self, request):
        data = request.POST
        new_movie = Movie.objects.create(
            title = data['title'],
            sinopsis = data['sinopsis'],
            duration = data['duration'],
            calif = data['calif'],
            gender = data['gender']
        )
        #print(data)
        if new_movie:
            print('Pelicula creada con exito')
            return redirect('/movies/')
        else:
            print('La pelicula no se pudo crear')
            return redirect('/movies/create/')
'''

'''
#class CreateMovieEasy(views.View):
    def get(self, request):
        form = MovieForm()
        template_name = 'movies/form_easy.html'
        context = {
            'form': form
        }
        return render(request, template_name, context)

    def post(self, request):
        new_form = MovieForm(request.POST)
        if new_form.is_valid():
            new_movie = new_form.save()
            print('Se creó la pelicula correctamente', new_movie)
            return redirect('/movies/')
'''



