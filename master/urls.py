from django.urls import path
from . import views

app_name = 'master'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('map/', views.map_view, name='map'),
    path('ai-engine/', views.ai_engine_view, name='ai_engine'),
    path('analytics/', views.analytics_view, name='analytics'),
    path('audit-trail/', views.audit_trail_view, name='audit_trail'),
    path('settings/', views.settings_view, name='settings'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('cost-budget/', views.cost_budget, name='cost_budget'),
    path('swept-path/', views.swept_path, name='swept_path'),
    path('analysis/', views.analysis, name='analysis'),
]
