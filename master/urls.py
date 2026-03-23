from django.urls import path
from . import views

app_name = 'master'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
