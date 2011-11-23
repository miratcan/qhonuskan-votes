from django import template

register = template.Library()

@register.filter
def is_up_voted_by(object, user):
    if user.is_authenticated():
        return bool(object.votes.filter(voter=user, value=1).count())
    else:
        return False

@register.filter
def is_down_voted_by(object, user):
    if user.is_authenticated():
        return bool(object.votes.filter(voter=user, value=-1).count())
    else:
        return False
