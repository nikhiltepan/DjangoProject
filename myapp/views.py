from django.shortcuts import render
from django.http import HttpResponse

def hello (request ):
    text ="<h1>Welcome to the app</h1>" 
    return HttpResponse(text)

def morning (request):
    text = "<h2>Its a nice morning</h2>"
    return HttpResponse(text)
# Create your views here.

