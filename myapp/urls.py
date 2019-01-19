# """helloapp URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/1.11/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.conf.urls import url, include
#     2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
# """
from django.conf.urls import url
from django.contrib import admin
from myapp import  views as app_views
from django.views.generic import TemplateView
from django.views.generic import ListView
from myapp import models

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     #url(r'^hello/', 'myapp.views.hello',name ='hello'),
#     url(r'^hello/', 'myapp.views.hello', name = 'hello'),
# # ]
from django.conf.urls import include,url
urlpatterns = [ url(r'^hello/$', (app_views.hello)  ),
                url(r'^morning/$',app_views.morning ),
                url(r'^$', app_views.home, name='home'),
                url(r'article/(\d+)/$', app_views.view_article, name='article'),
                url(r'article/(\d{2})/(\d{4})',app_views.view_article,name = 'article'),
                url(r'^simpleemail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',app_views.sendSimpleEmail,name='sendSimpleEmail'),
                url(r'^static/$',TemplateView.as_view(template_name='Static.html')),
                url(r'^dreamreals/',ListView.as_view(model=models.Dreamreal, template_name="dreamreal_list.html")),
                url(r'^connection/',TemplateView.as_view(template_name="login.html")),
                url(r'^login/',app_views.login,name='login') ]
                #  url(r'^static/$',app_views.StaticView.as_view()) ]
                # url(r'^dreamreals/',ListView.as_view( template_name="dreamreal_list.html")),model=models.Dreamreal, context_object_name=  ]



#url(r'^$',app_views.hello, name= 'hello'),