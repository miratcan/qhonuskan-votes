class QhonuskanVotesException(Exception):
    """
    All exceptions from qhonuskan_votes should inherit from this exception.
    """


class InvalidVoteModel(QhonuskanVotesException):
    """
    An invalid vote model was specified
    """
