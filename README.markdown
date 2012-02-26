#Qhonuskan-Votes

Easy to use reddit like voting system for django models.

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

After doing this, you can get your models with their scores by using
objects_with_scores manager. For example our first object in database upvoted
by three person. We would take score of object like this:

    ... : object = MyModel.objects_with_scores.get(id=1)
    ... : object.score
    ... : 3

### Extend your urls

To use the views for up voting and down voting you include the urls.py in your
website's url patterns. You can serve qhonuskan_votes views wherever you
want. Javascript files updates automatically to find qhonuskan_votes views.

	import qhonuskan_votes.urls
	from django.conf.urls.defaults import *

	urlpatterns = patterns('',
        ...
        ...
	    url(r'^votes/', include(qhonuskan_votes.urls)),
	)

### Extend your templates

Load qhonuskan_votes templatetags from your template, and you will need STATIC_PREFIX

    {% load qhonuskan_votes static %}
    {% get_static_prefix as STATIC_PREFIX %}

Load default_buttons.css to give little shape to buttons

    <link href="{{STATIC_PREFIX}}default_buttons.css" rel="stylesheet" type="text/css" />

After that line, if you wish you can override some properties

     <style type="text/css">
         div.vote_buttons {
             width: 40px;
             margin-right: 5px;
             float: left;
             border: 1px solid #666;
         }
    </style>

Load jquery to your template

    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>

After all, you can add voting_script template tag to your head section. It
generates necessary javascript code for ajax requests.

    {% voting_script %}

After doing these, you can use vote_buttons_for_object template tag to create
buttons.

    {% for object in objects %}
        <div class="object">
            {% vote_buttons_for object %}
            <div class="text">
                {{ object.text }}
            </div>
        </div>
    {% endfor %}
