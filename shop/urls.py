from django.urls import path
from .views import Shopping, About, Login

urlpatterns = [
    path('', Shopping, name="home"),
    path('about/', About, name="about"),
    path('login/', Login, name="login"),
    path('logout/', Login, name="logout"),
]