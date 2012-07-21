from django.db import models
from qhonuskan_votes.models import VotesField, ObjectsWithScoresManager
from qhonuskan_votes.models import vote_changed
from django.dispatch import receiver


class aModel(models.Model):
    """
    An example model for voting.
    """
    text = models.TextField()
    votes = VotesField()
    objects_with_scores = ObjectsWithScoresManager()

@receiver(vote_changed)
def my_callback(sender, dispatch_uid="vote_changed", **kwargs):
    print "vote_changed signal fired."
