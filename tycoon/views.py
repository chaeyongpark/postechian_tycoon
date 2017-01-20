#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Item, Avatar, Contain, Combination
from django.core import serializers

def home(request):
	return render(request, 'tycoon/home.html')

def combination(request):
	if request.method == 'GET':
		avatar = Avatar.objects.get(pk=1)
		class1_list = Contain.objects.filter(name__name__startswith='chaeyong').order_by('item')
		return render(request, 'tycoon/combination.html', {'avatar': avatar, 'clist': class1_list})
	
	elif request.method == 'POST':
		litem_cid = request.POST.get('left')
		litem = Contain.objects.get(id=litem_cid)
		ritem_cid = request.POST.get('right')
		ritem = Contain.objects.get(id=ritem_cid)
		
		try:
			nitem = Combination.objects.get(item1__name=litem.item.name, item2__name=ritem.item.name)
			print nitem.new_item
			print nitem.new_item.icon
			combined = {'id': Item.objects.get(name=nitem.new_item.name).id, 'url': nitem.new_item.icon.url}

		except :
			combined = {'id': 0, 'url': 'null'}

		finally:
			#res = serializers.serialize('json', combined)
			return JsonResponse({'nitem': combined})

def avatar(request):
	avatar = Avatar.objects.get(pk=1)
	return render(request, 'tycoon/avatar.html', {'avatar': avatar})

def codeToItem(request):
	return render(request, 'tycoon/codeToItem.html')

def mission(request):
	return render(request, 'tycoon/mission.html')

def itemBook(request):
	return render(request, 'tycoon/itemBook.html')
	
