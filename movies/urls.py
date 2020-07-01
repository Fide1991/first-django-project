from django.urls import path
#from .views. import GetMovies#, GetMovie, CreateMovie, CreateMovieEasy
from .views import GetMovies, GetMovie, CreateMovie, CreateMovieEasy, UpdateMovie, DeleteMovie

urlpatterns = [
    path('', GetMovies),
    path('<int:id>/', GetMovie),#ruta dinamica pora obtener un id y mandarlo a la view GetMovie
    #path('create/', CreateMovie.as_view())#se añade as_view porque es de tipo clase 
    path('create/',CreateMovieEasy.as_view()),
    path('update/<int:id>/', UpdateMovie.as_view()),
    path('delete/<int:id>/', DeleteMovie)
]
