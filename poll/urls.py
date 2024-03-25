from django.urls import path

from . import views

app_name = 'poll'

urlpatterns = [
    path('', views.index, name="index"),
    path('user/register/', views.register, name="register"),
    path('user/login/', views.login, name="login"),
    path('user/logout/', views.logout, name="logout"),
    path('user/update/', views.update, name="update"),
    path('vote/', views.vote, name="vote"),
]
