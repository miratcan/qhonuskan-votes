from django.db.models import aggregates
from qhonuskan_votes.models import _vote_models
from qhonuskan_votes.exceptions import InvalidVoteModel


def get_vote_model(model_name):
    if model_name in _vote_models:
        return _vote_models[model_name]
    else:
        raise InvalidVoteModel('No such vote model "%s"' % model_name)


class SumWithDefault(aggregates.Sum):
    name = 'SumWithDefault'
    template = 'COALESCE(%(function)s(%(field)s), %(default)s)'

setattr(aggregates, 'SumWithDefault',SumWithDefault)
