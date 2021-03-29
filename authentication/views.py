from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.



def index(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password =password  )

        if user is not None:
            auth.login(request , user)
            return redirect('/employee')    
        else:
            messages.info(request, 'Invalid username or password')
            return redirect("/")
    else:
        return render(request,'employee_register/index.html')


def register(request):

    if request.method == 'POST':

        email = request.POST['email']
        username = request.POST['username']
        password= request.POST['password']


        user = User.objects.create_user(username = username , password = password , email = email)
        user.save()
         
       
    
        
    return render(request,'employee_register/register.html')


def custom(request):
    return render(request, 'employee_register/custom.html')


def home(request):
    return render(request, 'employee_register/home.html')