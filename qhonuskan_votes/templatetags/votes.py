from django import template
from django.template import Variable
from django.template.loader import render_to_string
from django.db.models import Avg

register = template.Library()

from django_votes.models import VotesField
from django_votes.utils import get_vote_model

class VoteNode(template.Node):
    def __init__(self, object):
        self.object = object

    def get_info(self, context):
        variable = Variable(self.object)

        object = variable.resolve(context)

        self.model_name = '%s.%sVote' % (
            object._meta.app_label, object._meta.object_name,)

        self.model = get_vote_model(self.model_name)

        return object



class UpDownVoteNode(VoteNode):
    def render(self, context):
        object = self.get_info(context)
        total_votes = self.model.objects.filter(object__id=object.id).count()

        up_votes = self.model.objects.filter(
            object__id=object.id, value=1).count()
        down_votes = self.model.objects.filter(
            object__id=object.id, value= -1).count()
        up_pct = (float(up_votes) / float(total_votes) if total_votes else 0) * 98
        down_pct = (float(down_votes) / float(total_votes) if total_votes else 0) * 98
        dictionary = {
            'object': object,
            'model_name': self.model_name,
            'up_pct': up_pct,
            'down_pct': down_pct,
            'up_votes': up_votes,
            'down_votes': down_votes,
            'total_votes': total_votes}

        return render_to_string('django_votes/updownvote.html', dictionary, context_instance=context)

class RatingVoteNode(VoteNode):
    def render(self, context):
        object = self.get_info(context)

        avg = self.model.objects.filter(object__id=object.id).aggregate(value=Avg('value'))

        dictionary = {'rating': int(avg['value']) if 'value' in avg else None,
                      'object': object,
                      'model_name': self.model_name}

        return render_to_string('django_votes/rating.html', dictionary, context_instance=context)

@register.tag
def updown_vote(parser, token):
    args = token.split_contents()
    object = args[1]
    return UpDownVoteNode(object)

@register.tag
def rating_vote(parser, token):
    args = token.split_contents()
    object = args[1]
    return RatingVoteNode(object)

@register.filter
def is_up_voted_by(object, user):
    return bool(object.votes.filter(voter=user, value=1).count())

@register.filter
def is_down_voted_by(object, user):
    return bool(object.votes.filter(voter=user, value=-1).count())
