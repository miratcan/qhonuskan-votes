from django.views.generic import TemplateView
from django.template import RequestContext

from app.models import ThreadModel


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'objects': ThreadModel.objects_with_scores.all()
        })
        return context


home = HomeView.as_view()
