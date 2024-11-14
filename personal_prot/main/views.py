from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_views(request):
    background_color = None
    if request.method == 'POST' and 'change_bg' in request.POST:
        background_color = request.POST.get('change_bg')
    
    return render(request, 'main/changeBackground.html', {'background_color': background_color})
def about_views(request):
    return render(request, 'main/about.html')







