from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login  # Import for login function
from .forms import BirthdateForm

def home(request):
    # Your logic for the homepage
    return render(request, 'base/home.html')  # Example template path


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the newly created user
            return redirect("birthdate_form")  # Redirect to birthdate form view
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required
def birthdateView(request):
    if request.method=="POST":
        BirthdateForm=BirthdateForm(request.POST,request.FILES)
        if BirthdateForm.is_valid:
            BirthdateForm.save()    
    else:
        BirthdateForm=BirthdateForm()

    context={
    'form':BirthdateForm
    }    


    return render(request, "base/birthdate_form.html", context)
