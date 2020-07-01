from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import views
from .models import Movie
from .forms import MovieForm


# Hay dos formas de crear vistas
#1.- Creando una clase -> Tenemos dos o más métodos HTTP en la misma ruta 
#2.- Creando una funcion -> Solo tenemos un método HTTP en la ruta
def GetMovies(request):
    #vamos a traer todas las peliculas
    #SELECT * FROM movies_movie WHERE  seria la consulta equivalente, pero aqui se usa un ORM
    movies = Movie.objects.all()#queryset (es lo que el ORM retorna)
    #print(movies)
    #return HttpResponse('Funciona!')#para mostrar un texto en la pantalla y quitar la pantalla amarilla de error
    template_name = 'movies/list.html' #donde vive el template a renderizar
    context = {#se mandara la variable context al template (mandar datos de la view al template)
        'movies':movies
    }
    return render(request, template_name, context) #renderiza el template

def GetMovie(request,id):
    movie = Movie.objects.get(pk=id)#SELECT * FROM movies_movie WHERE id =
    template_name = 'movies/detail.html'
    context = {
        'movie': movie
    }
    return render(request, template_name, context)



class CreateMovie(views.View):
    def get(self, request):
        template_name = 'movies/form.html'
        return render(request, template_name)#no se le pasa contexto porque solo es un get

    def post(self, request):
        data = request.POST
        new_movie = Movie.objects.create(#equivalente a hacer un insert en la bd
            titulo = data['titulo'],
            sinopsis = data['sinopsis'],
            duracion = data['duracion'],
            calif = data['calif'],
            genero = data['genero']
        )
        #print(data)
        if new_movie:
            print('Pelicula creada con exito')
            return redirect('/movies/')
        else:
            print('La pelicula no se pudo crear')
            return redirect('/movies/create/')



class CreateMovieEasy(views.View):
    def get(self, request):
        form = MovieForm()
        template_name = 'movies/form_easy.html'
        context = {
            'form': form
        }
        return render(request, template_name, context)

    def post(self, request):
        new_form = MovieForm(request.POST)
        if new_form.is_valid():#validar que el formulario este correcrto
            new_movie = new_form.save()
            print('Se creó la pelicula correctamente', new_movie)
            return redirect('/movies/')
        else:
            template_name = 'movies/form_easy.html'
            context = {
                'form': new_form
            }
            return render(request, template_name, context)

class UpdateMovie(views.View):
    def get(self, request, id):
        movie = Movie.objects.get(pk=id)
        form = MovieForm(instance=movie)
        template_name = 'movies/form_easy.html'
        context = {
            'form': form,
            'id': id
        }
        return render(request, template_name, context)

    def post(self, request, id):
        movie = Movie.objects.get(pk=id)
        update_form = MovieForm(request.POST, instance=movie)
        if update_form.is_valid():
            form_updated = update_form.save()
            return redirect(f'/movies/{id}')
        else:
            template_name = 'movies/form_easy.html'
            context = {
            'form': update_form,
            'id': id
        }
        return render(request, template_name, context)

def DeleteMovie(request, id):
    movie = Movie.objects.get(pk=id)
    movie.delete()
    return redirect('/movies/')






