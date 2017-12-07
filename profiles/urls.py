from django.conf.urls import url

from .views import (
     ProfileDetailView
    )

urlpatterns = [
    #url(r'^create/$', ItemCreateView.as_view(), name='create'),
    #url(r'^(?P<pk>[\w-]+)/edit/$', ItemUpdateView.as_view(), name='edit'),
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
    #url(r'$', ItemListView.as_view(), name='list'),
    ]
