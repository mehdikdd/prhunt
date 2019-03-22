from django.shortcuts import render
from .models import Test


def home(request):
    obj = Test.objects.all()
    return render(request, 'products/home.html', {'c': obj})

