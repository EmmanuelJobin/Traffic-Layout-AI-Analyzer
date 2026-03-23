from django.shortcuts import render

def dashboard(request):
    return render(request, 'master/dashboard.html')

def recommendations(request):
    return render(request, 'master/recommendations.html')

def cost_budget(request):
    return render(request, 'master/cost_budget.html')

def swept_path(request):
    return render(request, 'master/swept_path.html')

def analysis(request):
    return render(request, 'master/analysis.html')
