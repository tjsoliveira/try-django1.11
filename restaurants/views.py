from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import RestaurantLocation

class RestaurantListView(ListView):

    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()

class CategoryRestaurantView(ListView):

    template_name = 'restaurants/restaurants_list.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(category__iexact=slug)
        else:
            queryset = RestaurantLocation.objects.none()
        return queryset

class RestaurantDetailView(DetailView):

    template_name = 'restaurants/restaurant_detail.html'
    queryset = RestaurantLocation.objects.all()

    # def get_object(self, *args, **kwargs):
    #     print(self.kwargs)
    #     rest_id = self.kwargs.get('pk')
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id)
    #     return obj
