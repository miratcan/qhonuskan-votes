from lettuce import *
from django.core.management import call_command
from django.urls import reverse
from django.test.client import Client
from app.models import ThreadModel


@before.all
def set_browser():
    world.browser = Client()

    call_command('syncdb', interactive=False, verbosity=0)


@step(u'following users exist:')
def given_following_users_exist(step):
    from qhonuskan_votes.compat import User

    for step_hash in step.hashes:
        user, created = User.objects.get_or_create(**step_hash)
        user.set_password('secret')
        user.save()


@step(u'I logined as "([^"]*)"')
def login(step, username):
    if username == 'I':
        pass

    from qhonuskan_votes.compat import User
    world.browser.login(username=username, password='secret')


@step(u'I access the url "([^"]*)"')
def access_url(step, url):
    response = world.browser.get(url)
    assert response.status_code == 200


@step(u'I tried to vote "([^"]*)"')
def access_voting(step, obj_id):
    vote_model = '%s.%sVote' % (
        ThreadModel._meta.app_label, ThreadModel._meta.object_name)
    voting_url = reverse('qhonuskan_vote')
    response_data = {
        'vote_model': vote_model,
        'object_id': obj_id,
        'value': 1
    }
    world.response = world.browser.post(voting_url, data=response_data)


@step(u'response status code is "([^"]*)"')
def then_vote_response_status_code_is(step, status_code):
    status_code = int(status_code)
    assert world.response.status_code == status_code
