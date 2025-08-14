from django.shortcuts import render
from chatbot.forms import UserForm
from django.views.decorators.csrf import csrf_exempt
import json
from .liebot_interface import query_llm

from django.http import HttpResponse
from django.http import JsonResponse

from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'LieBot/home.html')

def contact(request):
    return render(request, 'LieBot/contactus.html')

@csrf_exempt 
def get_chat_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            bot_reply = query_llm(user_message) if user_message else "Say something, twin 😏"
            return JsonResponse({'response': bot_reply})
        except Exception as e:
            return JsonResponse({'response': f"Error: {e}"})
    return JsonResponse({'response': 'Invalid request method'})


def register(request):
    #BASED ON CODE FROM DJANGO without profile included as that is not required for the scope of our project
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially. Code changes value to
    # True when registration succeeds.
    registered = False

    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm
        user_form = UserForm(request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to indicate that the template
            # registration was successful.
            registered = True
        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors)
    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request,
                  'LieBot/register.html',
                  context={'user_form': user_form,
                           'registered': registered})


def user_login(request):
    print("starting user login thing")
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
        # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return redirect(reverse('chatbot:home'))
            else:
            # An inactive account was used - no logging in!
                return HttpResponse("Your LieBot account is disabled.")
        else:
        # Bad login details were provided. So we can't log the user in.
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
        # The request is not a HTTP POST, so display the login form.
        # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'LieBot/login.html')
    
