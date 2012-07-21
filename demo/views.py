from django.shortcuts import render_to_response
from app.models import aModel
from django.template import RequestContext

def home(request):
    return render_to_response("home.html", {
        "objects": aModel.objects_with_scores.all()
    }, context_instance = RequestContext(request))
