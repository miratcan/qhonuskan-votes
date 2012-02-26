#Qhonuskan-Votes

Simple reddit like voting system for django models:

## How to use it?

### Append it to your models

Add qhonuskan_votes to your INSTALLED_APPS.

    INSTALLED_APPS = ('...',
                      '...',
                      'qhonuskan_votes')

    
Add VotesField, and add ObjectsWithScoresManager to your model.

    - Add the VotesField to your model:

    from django.db import models
    from qhonuskan_votes.models import VotesField

    class MyModel(models.Model):
        votes = VotesField()
        objects_with_scores = ObjectsWithScoresManager()
	...
	...

Syncdb.

    I think you can do this without an example. :)

After doing this, you can get your models with their scores by using objects_with_scores manager.
For example our first object in database upvoted by three person. We would take score of object like this:

    ... : object = MyModel.objects_with_scores.get(id=1)
    ... : object.score
    ... : 3



To use the views for up voting and down voting you include the urls.py in your website's url patterns:

	import qhonuskan_votes.urls
	from django.conf.urls.defaults import *

	urlpatterns = patterns('',
	    url(r'^votes/', include(qhonuskan_votes.urls)),
	)
	
...