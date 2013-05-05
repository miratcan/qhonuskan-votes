from django.db import models
from qhonuskan_votes.models import VotesField, ObjectsWithScoresManager
from qhonuskan_votes.models import vote_changed


class ThreadModel(models.Model):
    """
    An example model for voting.
    """
    text = models.TextField()
    votes = VotesField()

    objects = models.Manager()
    objects_with_scores = ObjectsWithScoresManager()


def my_callback(sender, **kwargs):
    print "vote_changed signal fired."

vote_changed.connect(my_callback, dispatch_uid="vote_changed")
