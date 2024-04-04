from django.shortcuts import render , redirect,HttpResponse, get_object_or_404
from .models import Customer, Product, Cart
from math import ceil
from PIL import Image # type: ignore
from django.core.exceptions import ValidationError
import re
from django.core.validators import validate_email


def validate_image_width(image):

    # Open the image using PIL or Pillow
    img = Image.open(image)
    # Get the width and height of the image
    width, height = img.size
    if width and height != 500:
        raise ValidationError("Image width and height must be 500 pixels.")

def validate_description_length(description):
    if len(description) > 100 and len(description) < 50:
        raise ValidationError("Description must be more than 50 land less than 100 characters long.")
    
def validate_phone_number_length(phone):
    phone_str = str(phone)  # Convert to string if it's not already
    if len(phone_str) != 10:
        raise ValidationError("Phone Number must be equal to 10 Digits.")


def checkemail(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        emailResult=True
    else:
        emailResult=False

    return emailResult

def passwordvalidation(password):
    regex=re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
    if re.fullmatch(regex, password):
        passwordResult=True
    else:
        passwordResult=False
    return passwordResult

def signup(request):
    if request.method =='POST':
        uname = request.POST['username']
        dob = request.POST['dob']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        images = request.FILES.get('image')
        phone = request.POST['phone']
        gender = request.POST['gender']
        user = Customer.objects.filter(Email = email)

        if user:
            return render(request, "Signup.html",{'error':'Your Email has been exist'})
        
        else:
            if password == repassword:
                    emailResult = checkemail(email)
                    password = passwordvalidation(password)
                    if emailResult:
                        if password:
                            try: 
                                validate_phone_number_length(phone)
                                newuser = Customer.objects.create(Username=uname,Email=email,password=password,phone_Number=phone, Gender=gender ,Date_of_birth=dob,image=images)
                                if newuser:
                                    return redirect('login')
                            except ValidationError as e:
                                return render(request, "Signup.html",{'error':e})
                        else:
                            return render(request, "Signup.html",{'error':'''
                                                                Requires at least one lowercase letter.
                                                                Requires at least one uppercase letter.
                                                                Requires at least one digit.
                                                                Requires at least one special character among @$!%*?&.
                                                                '''})
                    else:
                        return render(request, "Signup.html",{'error':'Please put the valid email'})

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
    return render (request , "HomePage.html", params)

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        users = Customer.objects.filter(Username=uname, password=password)
        if users.exists():
            user = users.first()
            # Assuming there's only one user with matching credentials
            return redirect('customer', id=user.id)
        else:
            return render(request, "loginin.html", {'error': 'Username or Password is invalid'})
    return render(request, "loginin.html")

def incard(request, product_id):
    if product_id is not None:  # Check if product_id is provided
        try:
            product = Product.objects.get(pk=product_id)
            # Assuming you have a serializer to serialize product details
            serialized_product = {
                'name': product.Product_Name,
                'publish': product.Product_pub,
                'price': product.Product_Price,
                'desc': product.Description,
                'location': product.Location,
                'image': product.image,
                'phone': product.Phone_Number
            }
            return render(request, "incard.html", {'serialized': serialized_product})
        except Product.DoesNotExist:
            return HttpResponse("Product not found")
    else:
        return HttpResponse("Product ID not provided in URL")

def profile(request,profile_id):

    customer = get_object_or_404(Customer, id=profile_id)
    customer_dict = {
        'id':customer.id,
        'username': customer.Username,
        'gender': customer.Gender,
        'phone':customer.phone_Number,
        'image':customer.image,
        'email':customer.Email,
        'pass':customer.password
    }

    if request.method =='POST':
        uname = request.POST['username']
        email = request.POST['email']
        passs = request.POST['password']
        phone = request.POST['phone']
        gender = request.POST['gender']
        images = request.FILES.get('images')
        customer.Username=uname
        customer.Gender=email
        customer.phone_Number=phone
        customer.Email=email
        customer.Gender=gender
        customer.password=passs
        customer.image=images
        customer.save()
        return redirect('profile',profile_id=customer.id)

    return render (request , "profile.html",{'customer_details':customer_dict})

def addcart(request,id,product_id): 
    
    cart = Cart.objects.filter(customer_id=id)

    cart_count = cart.count() 
    if request.method=='POST':
        product= get_object_or_404(Product, id=product_id)
        name = product.Product_Name
        price = product.Product_Price
        desc = product.Description
        images = product.image
        cus_id = id

        Cart.objects.create(Product_Name=name,Product_Price=price,Description=desc,customer_id=cus_id,image=images)
        return redirect('cart',id=cus_id)

    return render (request , "cartDetails.html",{'customer_items': cart,'cart_items':cart_count})

def CustomerPage(request, id):
    customer = get_object_or_404(Customer, id=id)
    
    allProds =[]
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nSlides), nSlides])
        params =  {'allProds':allProds,'id':id,'image':customer.image.url}

    if request.method =='POST':
        uname = request.POST['productName']
        Price = request.POST['price']
        description = request.POST['description']
        category = request.POST['category']
        phone = request.POST['phone']
        location = request.POST['location']
        photo = request.FILES.get('images')
        cus_id = id
        if photo:
            try:
                phone = int(phone)
            except ValueError:
                error_message = "Phone number must be an integer."
                params =  {'allProds':allProds,'error':error_message}
                return render(request, "CustomerPage.html", params)
            try:
                validate_image_width(photo)
            except ValidationError as e:
                params =  {'allProds':allProds,'error':e}
                return render(request, "CustomerPage.html",params)
            try:
                validate_description_length(description)
            except ValidationError as e:
                params =  {'allProds':allProds,'error':e}
                return render(request, "CustomerPage.html",params)  #
            try:
                validate_phone_number_length(phone)
            except ValidationError as e:
                params =  {'allProds':allProds,'error':e}
                return render(request, "CustomerPage.html",params)
            
            new_product = Product.objects.create(
            Product_Name=uname,
            Product_Price=Price,
            Description=description,
            Phone_Number=phone,
            Location=location,
            category=category,
            image=photo,
            customer_id=cus_id
            )

            if new_product:
                return redirect('customer',id=id) 
            
    return render (request , "CustomerPage.html",params)

def items(request,items_id):

    customer_items = Product.objects.filter(customer_id=items_id)
    if request.method =='POST':
        product = get_object_or_404(Product, id=items_id)
        product.delete()
        return redirect('items',items_id=product.customer_id)

    return render(request,"items.html",{'customer_items': customer_items,'id':items_id})

def editItem(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    product_dict = {
        'id':product.id,
        'name': product.Product_Name,
        'desc': product.Description,
        'price':product.Product_Price,
        'location':product.Location,
        'phone':product.Phone_Number,
        'cat':product.category,
        'image':product.image
    }
    if request.method =='POST':
        uname = request.POST['productName']
        price = request.POST['price']
        desc = request.POST['description']
        cat = request.POST['category']
        loaction = request.POST['location']
        images = request.FILES.get('images')

        product.Product_Name=uname
        product.Product_Price=price
        product.Description=desc
        product.category=cat
        product.Location=loaction
        product.image=images

        product.save()
        return redirect('edititem',product_id=product.id)


    return render(request,"itemsDetails.html",{'customer_items': product_dict})

def cart(request,id): 
    cart = Cart.objects.filter(customer_id=id)
    customer_id = id
    cart_count = cart.count()
    if request.method =='POST':
        cart = get_object_or_404(Cart, id=id)
        cart.delete()
        return redirect('cart',id=cart.customer_id)

    return render (request , "addCart.html",{'customer_items': cart,'cart_items':cart_count,'id':customer_id})

def seecart(request, product_id):
    if product_id is not None:  # Check if product_id is provided
        try:
            cart = Cart.objects.get(pk=product_id)
            # Assuming you have a serializer to serialize product details
            serialized_product = {
                'name': cart.Product_Name,
                'price': cart.Product_Price,
                'desc': cart.Description,
                'image': cart.image,
                'phone': cart.Phone_Number
            }
            return render(request, "seecart.html", {'serialized': serialized_product})
        except Product.DoesNotExist:
            return HttpResponse("Product not found")
    else:
        return HttpResponse("Product ID not provided in URL")
    
