from django.shortcuts import render
from django.http import HttpResponse
from blog import models
from .models import Catalog
def post_details(request):
    return HttpResponse('Hello Request Recieved')
obj=Catalog()
def show_details(request):
    return HttpResponse(Catalog.objects.all())
def personal_details(request):
    b=Catalog.objects.all()[0]
    return render(request,'temp.html',{'name':b.product_name})


def usn(request):
    class Details:
        def __init__(self, usn, name, city):
            self.usn = usn
            self.name = name
            self.city = city

    c = Catalog.objects.all()[0]

    a=Details(134,'Bharath','Bangalore')
    b=Details(83,'Likith','Malur')
    return render(request,'temp.html',{'name0':a.name,'name1':b.name,'usn0':a.usn,'usn1':b.usn,'city0':a.city,'city1':b.city,'name':c.product_name})



# Create your views here.
