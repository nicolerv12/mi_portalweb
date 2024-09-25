from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Bienvenido a tu pagina")
    return render(request, 'myapp/home.html')
def about(request):
    #return HttpResponse("Esta es la sección sobre nosotros")
    return render(request, 'myapp/about.html')
def contact(request):
    #return HttpResponse("Esta es la sección de contacto")
    return render(request, 'myapp/contact.html')
def blog(request):
    #return HttpResponse("Esta es la sección del blog")
    return render(request, 'myapp/blog.html')
def servicios(request):
    #return HttpResponse("Esta es la sección de servicios")
    return render(request, 'myapp/servicios.html')
# Create your views here.
