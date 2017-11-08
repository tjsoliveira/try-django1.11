import random
from django.shortcuts import render
from django.views import View

# function based view
def home(request):
    some_list = [random.randint(0, 10000), random.randint(0, 10000), random.randint(0, 10000)]
    context = {
        'html_var': 'context variable',
        'random_num': random.randint(0, 10000),
        'some_list': some_list
    }
    return render(request,'home.html', context)

def about(request):
    context = {
    }
    return render(request,'about.html', context)

class ContactView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request,"contact.html", context)
