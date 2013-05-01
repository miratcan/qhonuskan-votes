from lettuce import *
from django.core.urlresolvers import reverse
from django.test.client import Client
from app.models import ThreadModel


@before.all
def set_browser():
    world.browser = Client()


@step(u'Given I access the url "([^"]*)"')
def access_url(step, url):
    response = world.browser.get(url)
    assert response.status_code == 200
    

@step(u'Then I cannot vote "([^"]*)"')
def access_voting(step, obj_id):
    voting_url = reverse('qhonuskan_vote')
    response = world.browser.post(voting_url)
    
    import ipdb; ipdb.set_trace()
    thread = ThreadModel.objects.get(id=int(obj_id))
    import ipdb; ipdb.set_trace()
