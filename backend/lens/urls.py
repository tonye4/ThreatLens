from django.urls import path
from . import views

urlpatterns =[
    path('home', views.home),
    path('', views.home),
    path('api/comments/', views.reputation_score_view, name="reputation_score"),
]


