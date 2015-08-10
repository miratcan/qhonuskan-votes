from django.shortcuts import render
from app.models import ThreadModel
from django.template import RequestContext


def home(request):
    context_data = {'objects': ThreadModel.objects_with_scores.all()}
    return render(request,'home.html', context_data)
