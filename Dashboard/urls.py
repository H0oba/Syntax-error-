from django.urls import path
from . import views


# URLConfig
urlpatterns = [
    path('<int:pk>/', views.dashboard),
]
