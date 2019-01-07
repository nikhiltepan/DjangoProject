from django.core.mail import send_mail,EmailMessage
from myapp.models import Dreamreal
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
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
    # return render (request, "Hello.html",{"today": today, "days_of_week": days})
    return HttpResponseRedirect("Http://Djangoproject.com")


# def home (request):
#     text="<h1>Welcome to the app</h1>"    
#     return HttpResponse(text)

def view_article(request,article_Id):
    text = "Displaying the article number : %s" %article_Id
    return HttpResponse(text)

def view_article(request, month , year):
    text ="Displaying the articles of %s/%s"%(year, month)
    return HttpResponse(text)

def crudops(request):
    dreamreal = Dreamreal(website= "www.polo.com", mail = "sorex@polo.com", name= "sorax", phonenumber= "9954875136")
    dreamreal.save()

    objects = Dreamreal.object.all()
    res = 'printing all dreamreal entities in the DB : <br>'

    for elt in objects:
        res+=elt.name+"<br>"
    
    sorex = Dreamreal.objects.get(name="sorex")
    res+='Printing one entry <br>'
    res+=sorex.name

    #deleting an entry 
    res+='<br> Deleting an entry'
    sorex.delete

    #update 
    dreamreal=Dreamreal(website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"   )
    
    dreamreal.save()
    res+='updating entry <br>'

    dreamreal =Dreamreal.objects.get(name='sorex')
    dreamreal.name  = 'thierry'
    dreamreal.save()

    return HttpResponse(res)

def datamanupulation(request):
    res=''

    #filtering data
    qs = Dreamreal.objects.filter(name="paul")

    for elt in qs:
        res+=elt.name +'<br>'
    return HttpResponse(res)

def sendSimpleEmail(request, emailto):
    # res=send_mail("Subject","Yoo bro","Nikhiltepan102@gmail.com",[emailto])
    res = EmailMessage(subject="This is system generated mail do not reply.", body="bcbcbcbcbc", to=[emailto])
    res.send()

    return HttpResponse('<h1>Sent successfully<h1>')  #'%s'%res,


# Create your views here.

