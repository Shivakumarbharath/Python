from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
'''
Here We are using the same page for both the request 
i.e when the button register is clicked the register page is fetched
and when submit is clicked 

There fore here we use get and post methods to differentiate the both requests

when submitting data is a post request

and when register is called it is a get request

And thus use if else
'''

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(request,username=username,password=password)

        if user != None:
            auth.login(request,user)
            print("User logged")
            return redirect('/')


        else:
            messages.info(request,'Wrong Username or Password')

            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['FirstName']
        last_name = request.POST['LastName']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Existes")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                user.save()
                print('User Created')
                return render(request, 'login.html')
        else:
            messages.info(request,'Password not matcing')
            return redirect('register')
        #return redirect('/') this returns to the home page
    else:
        return render(request, 'register.html')