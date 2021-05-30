from django.views.generic.base import View
from django.http import HttpResponseRedirect


class AnalogView(View):
    def get(self, request):
        if 'analog' in request.session:
            request.session.pop('analog')
        else:
            request.session['analog'] = True
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
