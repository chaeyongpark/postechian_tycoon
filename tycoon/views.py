#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, Avatar, Contain

def home(request):
	return render(request, 'tycoon/home.html')

def combination(request):
	avatar = Avatar.objects.get(pk=1)
	class1_list = Contain.objects.filter(name__name__startswith='chaeyong').order_by('item')
	return render(request, 'tycoon/combination.html', {'avatar': avatar, 'clist': class1_list})
