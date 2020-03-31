from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add')#when ever the add is called in url then it goes to views.add function
]