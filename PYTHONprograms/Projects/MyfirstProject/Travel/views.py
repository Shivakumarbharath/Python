from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Travelindex.html')
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
