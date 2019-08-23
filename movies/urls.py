from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:Movie_pk>/', views.detail),
    path('<int:Movie_pk>/del', views.delete),
    path('<int:Movie_pk>/update', views.update),
    path('<int:Movie_pk>/upd', views.upd),
]