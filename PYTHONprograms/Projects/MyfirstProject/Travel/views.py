from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    #Destination1
    dest1=Destination()
    dest1.name='BENGALURU'
    dest1.price=10000
    dest1.desc='Best Destination to Pubs and Clubs'
    dest1.id='d001'
    dest1.img='destination_1.jpg'
    dest1.offer=True


    #DEstination2
    dest2 = Destination()
    dest2.name = 'HYDARABAD'
    dest2.price = 12000
    dest2.desc = 'Place Of Delicious Biriyani '
    dest2.id = 'd002'
    dest2.img='destination_2.jpg'
    dest2.offer = True

    # DEstination3
    dest3 = Destination()
    dest3.name = 'OOTY'
    dest3.price = 14000
    dest3.desc = 'Witness One Of The Blooming HillStations'
    dest3.id = 'd003'
    dest3.img='destination_3.jpg'
    dest3.offer = False

    # DEstination4
    dest4 = Destination()
    dest4.name = 'MUMBAI'
    dest4.price = 20000
    dest4.desc = 'The city that never sleeps'
    dest4.id = 'd004'
    dest4.img='destination_4.jpg'
    dest4.offer = False

    # DEstination5
    dest5 = Destination()
    dest5.name = 'GOA'
    dest5.price = 100000
    dest5.desc = 'Bunch Of Beaches'
    dest5.id = 'd005'
    dest5.img='destination_5.jpg'
    dest5.offer = True

    # DEstination4
    dest6 = Destination()
    dest6.name = 'Andaman&nicobar'
    dest6.price = 20000
    dest6.desc = 'The Island you have never seen'
    dest6.id = 'd006'
    dest6.img='destination_6.jpg'
    dest1.offer = False

    dests=[dest1,dest2,dest3,dest4,dest5,dest6]

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
