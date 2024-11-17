from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Main ,ContactMessage
from django.db.models import Q


# Create your views here.
def home_views(request):
    entries = Main.objects.all()
    
    context = {
        'entries': entries,
    }
    return render(request, 'main/main.html', context)

def about_views(request):
    entries = Main.objects.all()
    for entry in entries:
        entry.posters = [
            entry.poster,
            entry.poster2,
            entry.poster3,
            entry.poster4,
            entry.poster5,
        ]
        entry.posters = [poster for poster in entry.posters if poster and poster.url]
    
    context = {
        'entries': entries,
    }
    return render(request, 'main/about.html', context)
def contact_views(request):
    if request.method=="POST":
        new_contact= ContactMessage(
            title=request.POST.get('title'),
            email=request.POST.get('email'),
            message=request.POST.get('message'),
            )
        new_contact.save()
        return redirect('home_views') 
    return render(request,"main/contact.html")    
def contact_messages(request):
    messages = ContactMessage.objects.all().order_by('-submitted_at')
    context = {
        'messages': messages,
    }
    return render(request, 'main/messages.html', context)    
def create_views(request):
    if request.method=="POST":
        new_main= Main(
            titel=request.POST.get('titel'),
            short_reviwe=request.POST.get('short_reviwe'),
            email=request.POST.get('email'),
            about=request.POST.get('about'),
            poster=request.FILES.get('poster'),
            poster2=request.FILES.get('poster2'),
            poster3=request.FILES.get('poster3'),
            poster4=request.FILES.get('poster4'),
            poster5=request.FILES.get('poster5'),
        )
        new_main.save()
        return redirect('home_views') 
    return render(request,"main/create.html")    

def dashboard_views(request):
    query = request.GET.get('q', '').strip()
    ordering = request.GET.get('ordering', None)

    entries = Main.objects.all()

    if query:
        entries = entries.filter(
            Q(titel__icontains=query) |
            Q(short_reviwe__icontains=query) |
            Q(about__icontains=query)
        )

    allowed_ordering_fields = ['id', '-id', 'titel', '-titel', 'create_at', '-create_at']

    if ordering in allowed_ordering_fields:
        entries = entries.order_by(ordering)
    else:
        entries = entries.order_by('-create_at', 'id')  

    context = {
        'entries': entries,
    }
    return render(request, 'main/dashboard.html', context)


def update_views(request, entry_id):
    entry = get_object_or_404(Main, pk=entry_id)
    if request.method == "POST":
        entry.titel = request.POST.get('titel')
        entry.short_reviwe = request.POST.get('short_reviwe')
        entry.email = request.POST.get('email')
        entry.about = request.POST.get('about')
        if 'poster' in request.FILES:
            entry.poster = request.FILES.get('poster')
        if 'poster2' in request.FILES:
            entry.poster2 = request.FILES.get('poster2')
        if 'poster3' in request.FILES:
            entry.poster3 = request.FILES.get('poster3')
        if 'poster4' in request.FILES:
            entry.poster4 = request.FILES.get('poster4')
        if 'poster5' in request.FILES:
            entry.poster5 = request.FILES.get('poster5')
        entry.save()
        return redirect('dashboard_views')  
    return render(request, 'main/update.html', {'entry': entry})


def delete_views(request, entry_id):
    if request.method == "POST":
        try:
            entry = get_object_or_404(Main, pk=entry_id)
            entry.delete()
            print(f"Entry with ID {entry_id} deleted successfully.")
        except Exception:
            return HttpResponse("An error occurred while trying to delete the entry.")
    return redirect('dashboard_views')
def detail_views(request, user_id):
    entry = get_object_or_404(Main, pk=user_id)
  #To showen the poster in silder  
    entry.posters = [
        entry.poster,
        entry.poster2,
        entry.poster3,
        entry.poster4,
        entry.poster5,
    ]
    entry.posters = [poster for poster in entry.posters if poster]
    
    return render(request, 'main/details.html', {'entry': entry})

