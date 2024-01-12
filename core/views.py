from django.shortcuts import render

# Create your views here.
"""
Inicio/home
Productos/product
Tienda/store
Contacto/contact

"""

def home(request):
    return render(request, 'core/home.html')

def store(request):
    return render(request, 'core/store.html')

def contact(request):
    return render(request, 'core/contact.html')