from django.db import models
from qhonuskan_votes.models import VotesField, ObjectsWithScoresManager

class aModel(models.Model):
    """
    An example model for voting.
    """
    text = models.TextField()
    votes = VotesField()
    objects_with_scores = ObjectsWithScoresManager()
