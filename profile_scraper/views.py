from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Profile

# Create your views here.
def index(request):
    return render(request, 'profile_scraper/index.html')

def lookup(request, handle):
    #implement twitter api python program

def display(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    return render(request, 'profile_scraper/display.html', {'profile': profile})