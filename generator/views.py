from django.shortcuts import render
from django.http import HttpResponse
import random

def hello(request):
    return HttpResponse('Hello User!!!')

def home(request):
    return render(request,'generator/home.html')

def password(request):
    length = int(request.GET.get('length'))
    character = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        character.extend(list('0123456789'))
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*'))
    password = ''
    for i in range(length):
        password += random.choice(character)
    return render(request,'generator/password.html',{'password':password})


def about(request):
    return render(request,'generator/about.html')