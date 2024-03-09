from django.shortcuts import render

# Create your views here.
def HomePage(request):
    return render (request , "HomePage.html")

def login(request):
    return render (request , "loginin.html")

