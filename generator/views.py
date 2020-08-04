from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'gjgafgfjfajg2328'})

def password(request):
    thepassword = ''
    alphabet_string = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    characters = list(alphabet_string)
    if request.GET.get('uppercase'):
        characters.extend(list(alphabet_upper))
    if request.GET.get('special'):
        characters.extend(list("[@_!#$%^&*()<>?/\|}{~:]"))
    if request.GET.get('numbers'):
        characters.extend(list("0123456789"))
    length = int(request.GET.get('length',4))
    for i in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')
