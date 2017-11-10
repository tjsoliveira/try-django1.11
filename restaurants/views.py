from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render
from .models import RestaurantLocation
from .forms import RestaurantCreateForm
from django.http import HttpResponseRedirect

def restaurant_create_view(request):
    template_name = 'restaurants/restaurant_create_form.html'
    if request.method == "GET":
        print("get data")
    if request.method == "POST":
        print("post data")
        print(request.POST)
        name = request.POST.get("name")
        location = request.POST.get("location")
        category = request.POST.get("category")
        obj = RestaurantLocation.objects.create(
            name = name,
            location = location,
            category = category
        )
        return HttpResponseRedirect("/restaurants/")
    context = {}
    return render(request, template_name, context)

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
