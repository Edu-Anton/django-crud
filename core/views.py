from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request): # el request es la solicitud del cliente
  return render(request, "core/home.html")

def about(request):
  return render(request, "core/about.html")

def contact(request):
  return render(request, "core/contact.html")

def astrid(request):
  return HttpResponse("<h3>Área de mi hija Francesca</h3>")

def alonso(request):
  return HttpResponse("<h2>Área de mi hijo Alonso</h2>")
