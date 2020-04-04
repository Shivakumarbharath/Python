from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    # to accec destinations
    dests=Destination.objects.all()

    return render(request,'Travelindex.html',{'dests': dests})



def news(request):
    return render(request,'Travelnews.html')

def contact(request):
    return render(request,'Travelcontact.html')

def destinations(request):
    return render(request,'Traveldestinations.html')

def about(request):

    return render(request,'Travelabout.html')

def elements(request):
    return render(request,'Travelelements.html')
