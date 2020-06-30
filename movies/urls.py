from django.urls import path
#from .views. import GetMovies#, GetMovie, CreateMovie, CreateMovieEasy
from .views import GetMovies

urlpatterns = [
    path('', GetMovies)#,
    #path('<int:id>/', GetMovie),
    #path('create/')#, 
    #CreateMovie.as_view())
    #CreateMovieEasy.as_view())
]
