"""djangoProject_dz3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.http import HttpRequest, HttpResponse
import random


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Homepage')

def article_info(request: HttpRequest, article_id: int, article_slug: str) -> HttpResponse:
    try:
        int(article_id)
    except:
        return HttpResponse(f'article_id должен быть только int')
    return HttpResponse(f'Номер статьи №{article_id}, название статьи "{article_slug}"')

def password_examination(request: HttpRequest, password: str) -> HttpResponse:
    correct_data = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    if len(password) < 8:
        return HttpResponse('Пароль должен быть более 8 символот, а так же иметь только латинские буквы в любом регистре или же цифры')
    for i in password:
        if not i.upper() in correct_data:
            return HttpResponse('Пароль должен быть более 8 символот, а так же иметь только латинские буквы в любом регистре или же цифры')
    return HttpResponse('Пароль отвечает всем параметрам')

def generate_password(request: HttpRequest, length: int) -> HttpResponse:
    random_values = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''
    try:
        int(length)
    except:
        return HttpResponse(f'length должен быть только int')
    for i in range(int(length)):
        password += random.choice(random_values)
    return HttpResponse(f'Вот ваш сгенирированый пароль {password}')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home', home),
    path('homepage', home),
    path('article/<article_id>/<article_slug>', article_info),
    path('password/<password>', password_examination),
    path('password/generate/<length>', generate_password)
]