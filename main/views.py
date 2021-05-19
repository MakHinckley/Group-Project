from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return HttpResponse("Hello!! I'm working properly!")