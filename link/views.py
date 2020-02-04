from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import FormView

from RACTFXYZ import settings
from link.forms import LinkForm
from link.models import Link


def redirect_view(request, key):
    try:
        link = Link.objects.get(key=key)
        return redirect(link.link, permanent=True)
    except Link.DoesNotExist:
        return redirect(settings.FALLBACK_URL)


class RedirectView(LoginRequiredMixin, FormView):
    template_name = 'shorten.html'
    form_class = LinkForm
    success_url = '/'
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.save()
        return super(RedirectView, self).form_valid(form)
