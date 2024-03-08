from django.shortcuts import render

# Create your views here.
def HomePage(request):
    return render (request , "HomePage.html")


def register(request):
    return render(request,"signup.html")