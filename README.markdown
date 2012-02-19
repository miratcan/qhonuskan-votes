Description:
	Voting field and management views for rating. Usuable with any
	django model.

Usage example:
	- Add the VotesField to your model:

	from django.db import models
    from django_votes.models import VotesField

    class MyModel(models.Model):
	    votes = VotesField()
	    ... (  fields of this model)

To use the views for up voting and down voting you include the urls.py in your website's url patterns:

	import django_votes.urls
	from django.conf.urls.defaults import *

	urlpatterns = patterns('',
	    url(r'^votes/', include(django_votes.urls)),
	)

	Now you can use these views in your templates for down and up voting your objects:

	{% url my_result_view object.id as result_url %}

	<div class="votes" x:id="{{object.id}}" x:model-name="{{object.votes.model.get_model_name}}" x:url="{{result_url}}">
	    <ul>
	        <li><a href="#" class="vote-up" x:url="{% url votes_up_vote %}">{% trans "Vote up" %}</a></li>
	        <li><a href="#" class="vote-down" x:url="{% url votes_down_vote %}">{% trans "Vote down" %}</a></li>
	    </ul>
	    <div class="vote-results" style="display:none">
	    </div>
	</div>





