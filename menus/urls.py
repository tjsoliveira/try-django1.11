from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

from .views import (
    ItemCreateView,
    ItemDetailView,
    ItemListView,
    ItemUpdateView
    )

urlpatterns = [
    url(r'^create/$', ItemCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[\w-]+)/update/$', ItemUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[\w-]+)/$', ItemDetailView.as_view(), name='detail'),
    url(r'$', ItemListView.as_view(), name='list'),
    ]
