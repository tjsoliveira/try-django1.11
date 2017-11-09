from django.views.generic import ListView

from .models import RestaurantLocation

class RestaurantListView(ListView):

    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()

class DetailRestaurantView(ListView):

    template_name = 'restaurants/restaurants_list.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(category__iexact=slug)
        else:
            queryset = RestaurantLocation.objects.none()
        return queryset
