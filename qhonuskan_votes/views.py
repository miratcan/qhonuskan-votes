from django.contrib.auth.models import User
from qhonuskan_votes.utils import get_vote_model
from django.db.models import Sum
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect

def _api_view(func):
    """
    Extracts model information from the POST dictionary and gets the vote model
    from them.
    """

    def view(request):
        if request.method == 'POST':
            # Get comments model
            model_name = request.POST['vote_model']
            model = get_vote_model(model_name)
            object_id = request.POST['object_id']
            # View
            result = func(request, model, object_id, request.POST['value'])

            if result:
                return result
            else:
                # ... and redirect to next.
                if 'next' in request.REQUEST:
                    return HttpResponseRedirect(request.REQUEST['next'])
                else:
                    return HttpResponse('OK')
        else:
            # Default response: 403
            return HttpResponse(status=403)
    return view

@_api_view
def vote(request, model, object_id, value):
    """
    Likes or dislikes an item.
    """
    if not request.user.is_authenticated():
        return HttpResponse(status=401) # you are not authenticated
    try:
        value = int(value)
    except ValueError:
        return HttpResponse(status=400)

    if not value in (1, -1):
        return HttpResponse(status=400) # bad request

    try:
        vote_instance = model.objects.get(
            object__id=object_id, voter=request.user)
    except model.DoesNotExist:
        vote_instance = None

    if vote_instance:
        if vote_instance.value == value:
            vote_instance.delete()
            value = 0 # we voted as 0
        else:
            vote_instance.value = value
            vote_instance.save()
    else:
        vote_instance = model.objects.create(
            object_id=object_id, voter=request.user, value=value)

    response_dict = model.objects.filter(\
        object__id=object_id).aggregate(score=Sum("value"))

    if response_dict['score'] == None:
        response_dict['score'] = 0;

    response_dict.update({"voted_as": value})
    return HttpResponse(\
        simplejson.dumps(response_dict), mimetype="application/json")
