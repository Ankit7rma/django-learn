from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    path = request.path
    return HttpResponse(path,content_type="text/html", charset="utf-8")
def menuitems(request, dish):
    items =  {
        'pasta':'ha pasta h',
        'mango':'ha mango h'
        }
    description = items[dish]
    return HttpResponse(f"<h2>{dish}</h2>" + description)