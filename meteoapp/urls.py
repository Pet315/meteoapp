from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('show_db/', views.show_db, name='show_db'),
]