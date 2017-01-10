from django.shortcuts import render
from django.http import HttpResponse

from .models import Item

def home(request):
	return render(request, 'tycoon/home.html')

def combination(request):
	item = Item.objects.get(pk=1)
	return render(request, 'tycoon/combination.html', {'item': item})
