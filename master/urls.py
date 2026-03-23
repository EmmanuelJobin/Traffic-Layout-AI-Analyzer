from django.urls import path
from . import views

app_name = 'master'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('cost-budget/', views.cost_budget, name='cost_budget'),
    path('swept-path/', views.swept_path, name='swept_path'),
    path('analysis/', views.analysis, name='analysis'),
]
