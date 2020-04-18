from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class home_page_view(TemplateView):
    template_name = 'pages/index.html'


class about_page_view(TemplateView):
    template_name = 'pages/about.html'
