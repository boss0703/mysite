import logging
from django.views.generic import TemplateView, FormView
from . import forms
from .models import ImageFile

logger = logging.getLogger('development')


class IndexView(TemplateView):
    template_name = "discrimination/index.html"


class ResultView(FormView):
    model = ImageFile
    template_name = "discrimination/result.html"
    form_class = forms.DiscriminationForm
    success_url = "/result"

    def post(self, request, *args, **kwargs):
        # if self.request.POST.get('inputFile', None):
        #    logger.debug(self.request.POST.get('inputFile', None), None)
        logging.basicConfig(level=logging.DEBUG)
        logger.debug("-- call post --")

        logger.debug(request.POST.get('inputFile'))
        return self.get(request, *args, **kwargs)
