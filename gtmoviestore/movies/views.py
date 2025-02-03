from django.shortcuts import render
from .models import Movie

def index(request):
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = Movie.objects.all()
    return render(request, 'movies/index.html',
                  {'template_data': template_data})

# Create your views here.
