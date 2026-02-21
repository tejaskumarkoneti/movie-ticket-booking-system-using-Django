from rest_framework import generics
from .models import Movie, Theater, Showtime
from .serializers import MovieSerializer, TheaterSerializer, ShowtimeSerializer


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class TheaterListCreateView(generics.ListCreateAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer


class TheaterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer


class ShowtimeListCreateView(generics.ListCreateAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer


class ShowtimeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
