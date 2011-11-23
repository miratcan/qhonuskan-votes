from django import template

register = template.Library()

@register.filter
def is_up_voted_by(object, user):
    return bool(object.votes.filter(voter=user, value=1).count())

@register.filter
def is_down_voted_by(object, user):
    return bool(object.votes.filter(voter=user, value=-1).count())
