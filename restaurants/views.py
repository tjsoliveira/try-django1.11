from django.views.generic import ListView, DetailView, CreateView
from .models import RestaurantLocation
from .forms import RestaurantLocationCreateForm

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

class RestaurantCreateView(CreateView):

    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/restaurant_create_form.html'
    success_url = '/restaurants/'
