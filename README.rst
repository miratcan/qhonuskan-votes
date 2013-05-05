===============
Qhonuskan-Votes
===============

Easy to use reddit like voting system for django models.

Features
--------

*  Does not use GenericForeignKeys (which irritates me when making queries)
   Has vote_buttons_for templatetag, that generates html code for your object
   for vote buttons.

*  Has, default_buttons.css which gives a shape your buttons as default, but
   you can override.

*  Has, voting_script template tag, it generates javascript code to make
   ajax requests for voting. Automatically finds qhonuskan_votes views.

*  voting_script tag also renders overridable show_not_authenticated_error
   function, so you can use your own error windows (jquery-ui etc.) via
   overriding it.

*  Default buttons are pure css, there is no images. So it's lite.

What's new?
-----------
version 0.2
'''''''''''
* Defined ``get_version`` method to get project version in your code.
* Lettuce tests are added for testing voting system.
* Changed ``vote`` view name as ``qhonuskan_vote``. Prefix is required for
  minimizing view name conflicts.
* Moved templates to ``templates/qhonuskan`` directory.
* Minimum Django version that we supported is 1.3.


Quick Implementation Guide
--------------------------

1. Add qhonuskan_votes to your INSTALLED_APPS.

   ::

     INSTALLED_APPS = ('...',
                       '...',
                       'qhonuskan_votes')


2. Add **VotesField**, and add **ObjectsWithScoresManager** to your model.

   ::

     from django.db import models
     from qhonuskan_votes.models import VotesField

     class MyModel(models.Model):
         votes = VotesField()
	 # Add objects before all other managers to avoid issues mention in http://stackoverflow.com/a/4455374/1462141
	 objects = models.Manager()

	 #For just a list of objects that are not ordered that can be customized.
         objects_with_scores = ObjectsWithScoresManager()

	 #For a objects ordered by score.
	 sort_by_score = SortByScoresManager()
         ...
         ...

3. Syncdb.
4. Extend your urls [#]_.
   ::

     import qhonuskan_votes.urls
     from django.conf.urls.defaults import *

     urlpatterns = patterns('',
       ...
       ...
       url(r'^votes/', include(qhonuskan_votes.urls)),
     )

5. Create the list in you view. Use

   ::

     #For a regular list of items without votes from your model use the following:
     item_list_no_score = Items.objects.all()

     #For a list with scores that can be customized with use the following:
     item_list_unordered_with_scores = Items.objects_with_scores.all()
     #to customize the order by a field unique to your model. So something like this:
     item_list_unordered_with_scores = Items.objects_with_scores.all().order_by(-date_created)

     #To obtain a list of items sorted by vote counts like (1,0,-1) like Reddit:
     item_list_ordered__scores = Items.sort_by_score.all()


6. Load qhonuskan_votes templatetags from your template. You will need STATIC_PREFIX too.

   ::

     {% load qhonuskan_votes static %}
     {% get_static_prefix as STATIC_PREFIX %}


7. Load default_buttons.css to give little shape to buttons

   ::

     <link href="{{STATIC_PREFIX}}default_buttons.css" rel="stylesheet" type="text/css" />

8. After that line, if you wish you can override some properties

   ::

     <style type="text/css">
       div.vote_buttons {
         width: 40px;
         margin-right: 5px;
         float: left;
         border: 1px solid #666;
       }
     </style>

9. Load jquery to your template

   ::

     <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>

10. After all, you can add voting_script template tag to your head section.
It generates necessary javascript code for ajax requests.

   ::

     {% voting_script %}

11. use vote_buttons_for_object template tag to create buttons.

    ::

      {% for object in objects %}
        <div class="object">
          {% vote_buttons_for object %}
            <div class="text">
              {{ object.text }}
            </div>
        </div>
      {% endfor %}

For further information you can inspect example project at root of the repository.

Contribution
------------
You liked this project? Nice. Let's start with provide your virtual
environment. You can install all you need dependencies::

    $ pip install -r requirements/development.txt

We have some important conditions during the development of the project:

* We adopt PEP8 as Python style guide.
* You can send us patch for reviewing changes, but if you fork the project
  and open a pull request from github, that would be very easy for us.


FootNotes
---------
.. [#] To use the views for up voting and down voting you include the urls.py in your
       website's url patterns. You can serve qhonuskan_votes views wherever you
       want. Javascript files updates automatically to find qhonuskan_votes views.
