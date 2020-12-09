from django.shortcuts import render, HttpResponse, redirect
from apps.login.models import User
from .models import *
from django.contrib import messages
import bcrypt
import datetime

def index(request):
    if "currentuser" not in request.session:
        messages.error(request, "Please login")
        return redirect ("/")
    try: 
        userIn = User.objects.get(id = request.session["currentuser"])
    except:
        messages.error(request, "Please check your password/email combination!")
        return redirect ("/")
    allPosts = Trip.objects.all()
    myposts = userIn.tripsassigned.all()
    try:
        unassigned = User.objects.get(email = "none@none.com")
    except:
        unassigned = User.objects.create(first_name = "None", last_name= "None", email="none@none.com", password = "none")
    available = unassigned.trips.all()
    context = {
        "current": userIn,
        "allPosts": allPosts,
        "myposts": myposts,
        "unassigned": unassigned,
    }

    return render(request, "main/index.html", context)

def trippost(request):
    form = request.POST
    errors = Trip.objects.basic_validator(form)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect ("/wall/create")

    currentuser = User.objects.get(id=request.session["currentuser"])
    unassigned = User.objects.get(email = "none@none.com")
    Trip.objects.create(destination = form["destination"],plan = form["plan"],user = currentuser, start_date = form["start_date"], end_date = form["end_date"], userassigned = currentuser)
    return redirect ("/wall" )



def viewtrip(request, tripid):
    userIn = User.objects.get(id = request.session["currentuser"])
    context = {
        "trippost": Trip.objects.get(id=tripid),
        "current": userIn,
    }
    return render(request, "main/postinfo.html", context)

def addtrip(request, tripid):
    trip = Trip.objects.get(id = tripid)
    trip.userassigned = User.objects.get(id= request.session["currentuser"])
    trip.save()

    return redirect ("/wall")

def edittrip(request, tripid):
    trip = Trip.objects.get(id = tripid)
    current = User.objects.get(id= request.session["currentuser"])
    context = {
        "currenttrip": trip,
        "current": current,
    }
    return render (request, "main/edit.html", context)


def updatetrip(request, tripid):
    form = request.POST
    errors = Trip.objects.edit_validator(form)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect (f"/wall/{tripid}/edittrip")
    trip = Trip.objects.get(id = tripid)
    trip.destination = form["destination"]
    trip.plan = form["plan"]
    trip.start_date = form["start_date"]
    trip.end_date = form["end_date"]
    trip.save()
    return redirect ("/wall")

def destroytrip(request, tripid):
    Trip.objects.get(id = tripid).delete()
    return redirect ("/wall")

def create(request):
    
    user = User.objects.get(id= request.session["currentuser"])

    context = {
        "current": user,
    }
    return render(request, "main/createpost.html", context)

def returntrip(request, tripid):
    trip = Trip.objects.get(id= tripid)
    trip.userassigned = User.objects.get(email = "none@none.com")
    trip.save()
    return redirect ("/wall")

def walldestroy(request):
    Trip.objects.all().delete()

    return redirect ("/wall")