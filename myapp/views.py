from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hello (request ):
    text ="<h1>Welcome to My App</h1>" 
    return HttpResponse(text)

def morning (request):
    text = "<h2>Its a nice morning</h2>"
    return HttpResponse(text)

def home (request):
    # template=loader.get_template('myapp/Template/Hello.html')
    days=["Mon", "Tue", "Wed", "Thus", "Fri", "Sat", "Sun"]
    today = datetime.datetime.now().date()
    return render (request, "Hello.html",{"today": today, "days_of_week": days})


# def home (request):
#     text="<h1>Welcome to the app</h1>"    
#     return HttpResponse(text)

def view_article(request,article_Id):
    text = "Displaying the article number : %s" %article_Id
    return HttpResponse(text)

def view_article(request, month , year):
    text ="Displaying the articles of %s/%s"%(year, month)
    return HttpResponse(text)


# Create your views here.

