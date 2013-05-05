from django.shortcuts import render_to_response
from app.models import ThreadModel
from django.template import RequestContext


def home(request):
    context_data = {'objects': ThreadModel.objects_with_scores.all()}
    return render_to_response(
        'home.html', context_data, context_instance=RequestContext(request))
