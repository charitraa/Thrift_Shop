from django.shortcuts import render

# Create your views here.
def HomePage(request):
    return render (request , "HomePage.html")

def login(request):
    return render (request , "loginin.html")

def card(request):
    return render (request , "card.html")

def incard(request):
    return render (request , "incard.html")

def form(request):
    return render (request , "form.html")