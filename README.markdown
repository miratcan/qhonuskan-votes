#Qhonuskan-Votes

Simple reddit like voting system for django models:

## How to use?

### Add VotesField, and add ObjectsWithScoresManager to your model

    - Add the VotesField to your model:

    from django.db import models
    from qhonuskan_votes.models import VotesField

    class MyModel(models.Model):
        votes = VotesField
        objects_with_scores = ObjectsWithScoresManager()
	... (  fields of this model)

To use the views for up voting and down voting you include the urls.py in your website's url patterns:

	import qhonuskan_votes.urls
	from django.conf.urls.defaults import *

	urlpatterns = patterns('',
	    url(r'^votes/', include(qhonuskan_votes.urls)),
	)
	
...