from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'LieBot/home.html')

def contact(request):
    return render(request, 'LieBot/contactus.html')

def login(request):
    return render(request, 'LieBot/login.html')

def signup(request):
    return render(request, 'LieBot/signup.html')    