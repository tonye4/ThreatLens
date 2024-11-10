from django.urls import path
from . import views
from .views import test_connection

urlpatterns =[
    path('list/', views.get_languages, name='get_languages'),
    path('api/ping/', views.ping),
    path('api/test/', test_connection, name='test_connection'),
]



