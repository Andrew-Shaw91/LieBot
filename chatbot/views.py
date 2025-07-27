from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'LieBot/home.html')

def contact(request):
    return render(request, 'LieBot/contactus.html')