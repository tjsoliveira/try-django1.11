from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

from .views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView,
    )

urlpatterns = [
    url(r'^create/$', RestaurantCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='detail'),
    url(r'$', RestaurantListView.as_view(), name='list'),
    ]
