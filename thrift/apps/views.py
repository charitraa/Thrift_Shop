from django.shortcuts import render , redirect
from .models import Customer, Product
from math import ceil
from PIL import Image # type: ignore
from io import BytesIO
from django.core.exceptions import ValidationError

def validate_image_width(image):
    # Open the image using PIL or Pillow
    img = Image.open(image)
    # Get the width and height of the image
    width, height = img.size
    if width != 400:
        raise ValidationError("Image width must be 500 pixels.")


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
    allProds =[]
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nSlides), nSlides])
        params =  {'allProds':allProds}
    if request.method =='POST':
        uname = request.POST['productName']
        Price = request.POST['price']
        description = request.POST['description']
        category = request.POST['category']
        phone = request.POST['phone']
        location = request.POST['location']
        photo = request.FILES.get('images')
        if photo:
            try:
                validate_image_width(photo)
            except ValidationError as e:
                params =  {'allProds':allProds,'error':e}
                return render(request, "HomePage.html",params)        
            newproduct = Product.objects.create(Product_Name=uname,Product_Price=Price,Description=description,Phone_Number=phone, Location=location ,category=category,image=photo)
        if newproduct:
            return redirect('Home')

    return render (request , "HomePage.html", params)

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


def incard(request):
    return render (request , "incard.html")

def CustomerPage(request):
    return render(request,"CustomerPage.html")