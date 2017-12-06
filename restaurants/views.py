from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import RestaurantLocationCreateForm
from .models import RestaurantLocation

class RestaurantListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/restaurant_create_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/detail-update.html'

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantUpdateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Restaurant: ' + self.get_object().name
        return context
