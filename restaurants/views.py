#from django.shortcuts import render
from django.http import HttpResponse

# function based view
def home(request):
    #return render(request=request, template_name= 'home.html', {})
    return HttpResponse('Hello')
