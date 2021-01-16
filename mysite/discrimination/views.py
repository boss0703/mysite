from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from . import forms


class IndexView(TemplateView):
    template_name = "discrimination/index.html"


class ResultView(FormView):
    # def post():
    template_name = "discrimination/result.html"
    form_class = forms.DiscriminationForm
    success_url = "discrimination/result.html"
