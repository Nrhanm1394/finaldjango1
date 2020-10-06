from django.shortcuts import render
from .models import Product
# from django.http import HttpResponse
# Create your views here.
def base(request):
    # html = "<html><body>hello to my work </body></html>"
    return render (request,'frontend/base.html',)

def nature(request):
    return render (request,'frontend/nature.html')
def architecture(request):
    return render (request,'frontend/architecture.html')
def contact(request):
    return render (request,'frontend/contact.html')
    
