from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    d = {'data':"Django is big!"}
    list = [1,2,3,4,5]
    return render(request, 'data.html', {'d':d, 'list':list})