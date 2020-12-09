from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, "login/index.html")

def register(request):
    form = request.POST
    errors = User.objects.basic_validator(form)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect ("/")
    password = form["password"]
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    print(pw_hash)

    newUser = User.objects.create(
        first_name= form["first_name"],
        last_name=form["last_name"],
        email=form["email"],
        password=pw_hash
        )
    
    request.session["currentuser"] = newUser.id
    
    return redirect(f"/wall")

def login(request):
    form = request.POST

    errors = User.objects.login_validator(form)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect ("/")
    try:
        user = User.objects.filter(email=form["email"])
    except:
        messages.error(request, "Please check your email/password combination!")
        return redirect("/")
    try: 
        loggedIn = user[0]
        if bcrypt.checkpw(form["password"].encode(), loggedIn.password.encode()):
            request.session["currentuser"] = loggedIn.id
    except:
        messages.error(request, "Please check your email/password combination!")
        return redirect("/")
    return redirect(f"/wall")

def logout(request):
    request.session["currentuser"] = None

    return redirect("/")