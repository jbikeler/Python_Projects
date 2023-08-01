from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    products = ['Cherries', 'Apples','Oranges','Strawberries','Pears','Watermelons']
    names = ['Django', 'Bill','Grace','Jessie','Olivia','Jared']
    context = {
        'products': products,
        'names': names,
    }
    return render(request, 'home.html', context)