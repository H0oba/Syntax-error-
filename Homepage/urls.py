from django.urls import path,include
from . import views

app_name = 'Homepage'

urlpatterns = [
    path('', views.index, name='index'),
]
