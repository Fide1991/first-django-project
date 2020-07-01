from django.urls import path
#from .views. import GetMovies#, GetMovie, CreateMovie, CreateMovieEasy
from .views import GetMovies, GetMovie, CreateMovie, CreateMovieEasy

urlpatterns = [
    path('', GetMovies),
    path('<int:id>/', GetMovie),#ruta dinamica pora obtener un id y mandarlo a la view GetMovie
    #path('create/', CreateMovie.as_view())#se añade as_view porque es de tipo clase 
    path('create/',CreateMovieEasy.as_view())
]
