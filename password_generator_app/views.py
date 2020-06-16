from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'password_generator_app/home.html')

def passwordo(request):
    random_password = ''
    characters = list('abcdefghijklmnopqrstxyz')

    # if checkbox ('uppercase', 'numbers' etc.) is checked we extend the list:
    if request.GET.get("uppercase"):
        characters.extend('abcdefghijklmnopqrstxyz'.upper())
    if request.GET.get("special"):
        characters.extend('!@#$%^&*?')
    if request.GET.get("numbers"):
        characters.extend('1234567890')

    # we get password-lenght from home.html and by default it's string
    pass_len = int(request.GET.get('length', 12))
    for i in range(pass_len):
        random_password += random.choice(characters)

    # dictionary for connection between views.py and home.html
    return render(request, 'password_generator_app/passwordo.html', {"the_haslo":random_password})
