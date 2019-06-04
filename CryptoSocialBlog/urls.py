"""CryptoSocialBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.urls.conf import path
from django.contrib import admin
from django.views.generic import TemplateView
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
  #  url(r'', include('blog.urls')),
    path('accounts/', include('allauth.urls')),
    url(r'^post/remote/new/$', views.remote_post_new, name='remote_post_new'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    path('', TemplateView.as_view(template_name='blog/loginFacebook.html')),
    path('home/', TemplateView.as_view(template_name='blog/home.html')),
    url(r'^getprice/btc/$', views.get_price_btc, name='get_price_btc'),



]
