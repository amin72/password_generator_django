from django.shortcuts import render
import string
import random
from .forms import OptionsForm


def generate(request):
    form = OptionsForm(request.GET)
    password = ''
    if form.is_valid():
        cd = form.cleaned_data
        length = cd.get('length', 14)
        uppercase = cd['uppercase']
        special_chars = cd['special_chars']

        chars = string.ascii_lowercase + string.digits

        if uppercase:
            chars += string.ascii_uppercase
        
        if special_chars:
            chars += "!@#$%^&*()_+=-[]{}\\/.,:;"
        
        password = ''.join(random.choices(chars, k=length))

    context = {
        'form': form,
        'password': password
    }


    return render(request, 'generator/generate.html', context)
