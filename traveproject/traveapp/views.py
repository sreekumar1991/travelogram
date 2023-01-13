from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Person

def demo(request):
    obj=Place.objects.all()
    per=Person.objects.all()
    return render(request,"index.html",{'result':obj,"res":per})




# Create your views here.
