from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from main.alchemy_service.service import AlchemyService
from .forms import PostForm

def search(request):
    if request.method == 'POST':
        InputForm = PostForm(request.POST)
        if InputForm.is_valid():
            alchemy_service = AlchemyService()
            alchemy_service.getResults(request.POST['search'])
            return render(request, 'home.html', {'positive_articles': {}, 'negative_articles': {}, 'error': False})
        else:
            return render(request, 'home.html', {'error': True })
    else:
        form = PostForm()
        return render(request, 'home.html', {'form': form})
