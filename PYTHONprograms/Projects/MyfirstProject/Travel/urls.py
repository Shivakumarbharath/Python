from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    #path('add',views.add,name='add')#when ever the add is called in url then it goes to views.add function
    path('news.html',views.news,name='news'),
    path('destinations.html',views.destinations,name='destinations'),
    path('contact.html', views.contact, name='contact'),
    path('elemants.html', views.elements, name='elements'),
    path('about.html',views.about,name='about')
]