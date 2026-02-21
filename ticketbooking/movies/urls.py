from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', views.MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail'),
    path('theaters/', views.TheaterListCreateView.as_view(), name='theater-list-create'),
    path('theaters/<int:pk>/', views.TheaterRetrieveUpdateDestroyView.as_view(), name='theater-detail'),
    path('showtimes/', views.ShowtimeListCreateView.as_view(), name='showtime-list-create'),
    path('showtimes/<int:pk>/', views.ShowtimeRetrieveUpdateDestroyView.as_view(), name='showtime-detail'),
]