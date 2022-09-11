from django.urls import path
from . import views

app_name = 'app1'  # declaring the app_name here

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('second/', views.secondpage, name='secondpage'),
]
