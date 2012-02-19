from django.shortcuts import render_to_response
from app.models import aModel

def home(request):
    return render_to_response("home.html", {"objects": aModel.objects_with_scores.all()})
