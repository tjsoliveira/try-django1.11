import random
from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        #context = super(HomeView, self).get_context_data(*args, **kwargs)
        some_list = [random.randint(0, 10000), random.randint(0, 10000), random.randint(0, 10000)]
        context = {
            'html_var': 'context variable',
            'random_num': random.randint(0, 10000),
            'some_list': some_list
        }
        return context
