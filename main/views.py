from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
from django.db.models import Count

def index(request):
    return render(request,"index.html")

def registerPage(request):
    return render(request, "register.html")

def create_user(request):
    if request.method == "POST":
        errors = User.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], alias_gamert=request.POST['alias_gamert'], email=request.POST['email'], password=pw_hash)
            request.session['user_id'] = user.id
            return redirect('/welcome')
    return redirect('/')

def welcome(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'logged_user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, "welcome.html", context)

def login(request):
    if request.method == "POST":
        users_with_email = User.objects.filter(email=request.POST['email'])
        if users_with_email:
            user = users_with_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/welcome')
        messages.error(request, "Email or password are not right")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def recently_played(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, "welcome.html")