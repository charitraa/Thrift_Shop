from django.shortcuts import render , redirect
from .models import Customer
# Create your views here.

def signup(request):

    if request.method =='POST':
        uname = request.POST['username']
        dob = request.POST['dob']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        phone = request.POST['phone']
        gender = request.POST['gender']
        user = Customer.objects.filter(Email = email)

        if user:
            return redirect('signup')
        else:
            if password == repassword:
                newuser = Customer.objects.create(Username=uname,Email=email,password=password,phone_Number=phone, Gender=gender ,Date_of_birth=dob)
                if newuser:
                    return redirect('login')
                
    return render(request,"Signup.html")

# Create your views here.
def HomePage(request):
    return render (request , "HomePage.html")

def login(request):
    if  request.method =='POST':
        uname = request.POST['username']
        password = request.POST['password']
        user = Customer.objects.get(Username=uname)
        if user:
            if user.password == password:
                return redirect('Home')
        else:
            return redirect('login')
    return render (request , "loginin.html")

def card(request):
    return render (request , "card.html")

def incard(request):
    return render (request , "incard.html")

def form(request):
    return render (request , "form.html")

def profile(request):
    return render (request , "profile.html")