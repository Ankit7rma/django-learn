from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World , This is Home Page.")
def about(request):
    return HttpResponse("Hello World , This is About Page.")
def contact(request):
    return HttpResponse("Hello World , This is Contact Page.")