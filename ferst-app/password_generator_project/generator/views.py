import random

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    lst=list(range(6, 15))
    return render(request, 'generator/home.html', {'lst': lst})

def password(request):
    char = [chr(i) for i in range(97, 123)]
    if request.GET.get('uppercase'):
        char.extend([chr(i) for i in range(65, 91)])
    if request.GET.get('special'):
        char.extend([chr(i) for i in range(33, 48)])
    if request.GET.get('numbers'):
        char.extend([chr(i) for i in range(48, 58)])
    length = int(request.GET.get('length', 12))
    psw = ''
    for i in range(length):
        psw += random.choice(char)
    return render(request, 'generator/password.html', {'password': psw})

def about(request): # в request приходят данные из action  с html
    author = "Mariya"
    post = 'Для генерации пароля необходимо выбрать из выпадающего списка' \
          'длинну пароля (рекомендуемая длинна 12 символов)' \
          'так же возможно выбрать символы из которых будет состять пароль' \
          'помимо строчных латинских букв (цыфры, буквы в верзнем регистре или/и спецсимволы.' \
          'и нажатькнопку "сгенерировать пароль"'

    return render(request, 'generator/about.html', {'author': author, 'post': post})

