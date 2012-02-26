from django import template
from django.core.urlresolvers import reverse
from django.template import RequestContext

register = template.Library()


@register.inclusion_tag('voting_js.html')
def voting_script():
    return {"vote_url": reverse("vote")}

@register.filter
def is_up_voted_by(object, user):
    """
    If user is up voted given object, it returns True.
    """
    if user.is_authenticated():
        return bool(object.votes.filter(voter=user, value=1).count())
    else:
        return False

@register.filter
def is_down_voted_by(object, user):
    """
    If user is down voted given object, it returns True.
    """
    if user.is_authenticated():
        return bool(object.votes.filter(voter=user, value=-1).count())
    else:
        return False

@register.inclusion_tag('vote_buttons.html',takes_context=True)
def vote_buttons_for(context, object, *args, **kwargs):
    return {
        "user": context['user'],
        "object": object,
        "vote_model": "%s.%sVote" % (
            object._meta.app_label, object._meta.object_name)
    }
