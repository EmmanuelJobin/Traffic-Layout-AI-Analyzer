from django.shortcuts import render

def dashboard(request):
    return render(request, 'master/dashboard.html')

def map_view(request):
    return render(request, 'master/map.html')

def ai_engine_view(request):
    return render(request, 'master/ai_engine.html')

def analytics_view(request):
    return render(request, 'master/analytics.html')

def audit_trail_view(request):
    return render(request, 'master/audit_trail.html')

def settings_view(request):
    return render(request, 'master/settings.html')

def recommendations(request):
    return render(request, 'master/recommendations.html')

def cost_budget(request):
    return render(request, 'master/cost_budget.html')

def swept_path(request):
    return render(request, 'master/swept_path.html')

def analysis(request):
    return render(request, 'master/analysis.html')
