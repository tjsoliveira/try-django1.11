import random
from django.shortcuts import render

# function based view
def home(request):
    context = {
        'html_var': 'context variable',
        'random_num': random.randint(0, 10000)
    }
    return render(request,'base.html', context)
