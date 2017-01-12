from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from main.alchemy_service.service import AlchemyService
from .forms import PostForm

def search(request):
    if request.method == 'POST':
        alchemy_service = AlchemyService()
        print request
        #alchemy_service.getResults(request)
    #return HttpResponse("Hello, world. You're at the polls index.")
        return render(request, 'home.html', {'positive_articles': {}, 'negative_articles': {}})
    else:
        form = PostForm()

        return render(
            'home.html',
            {'form': form}
        )
