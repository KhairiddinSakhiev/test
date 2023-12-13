from django.urls import path

from apis.views import MovieListCreateAPIView, ActorListCreateAPIView, MovieRetrieveUpdateDestroyView

urlpatterns = [
    path("", MovieListCreateAPIView.as_view()),
    path("<int:pk>", MovieRetrieveUpdateDestroyView.as_view()),
    path("mov", ActorListCreateAPIView.as_view()),
]
