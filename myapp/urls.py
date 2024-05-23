# myapp/urls.py
from django.urls import path
from .views import MovieListAPIView, MovieDetailAPIView, create_fake_movies, CastMemberDetailAPIView, \
    CastMemberListAPIView, user_login, UserDetailAPI, RegisterUserView, LoginView, UserView, LogoutView

urlpatterns = [
    path('movies/', MovieListAPIView.as_view(), name='movie-list'),  # Maps to "/"
    path('movies/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),  # Maps to "/movie/:movieId"
    path('create/fake/movies/', create_fake_movies, name='create-fake-movies'),
    path('castmembers/', CastMemberListAPIView.as_view(), name='castmembers-list'),
    path('castmembers/<int:pk>/', CastMemberDetailAPIView.as_view(), name='castmembers-list'),
    path('login/', LoginView.as_view(), name='login'),
    # path('register/', register_user, name='signup'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('user/', UserView.as_view(), name='user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("get-details", UserDetailAPI.as_view()),
]
