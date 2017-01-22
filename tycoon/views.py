#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Item, Avatar, Contain, Combination, CodeToItem
from django.views.decorators.csrf import csrf_protect

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
			combined = {'id': Item.objects.get(name=nitem.new_item.name).id, 'url': nitem.new_item.icon.url}
		except :
			try:
				nitem2 = Combination.objects.get(item2__name=litem.item.name, item1__name=ritem.item.name)
				combined = {'id': Item.objects.get(name=nitem2.new_item.name).id, 'url': nitem2.new_item.icon.url}
			except:
				combined = {'id': 0, 'url': 'null'}

		finally:
			return JsonResponse({'nitem': combined})

def avatar(request):
	avatar = Avatar.objects.get(pk=1)
	return render(request, 'tycoon/avatar.html', {'avatar': avatar})

def codeToItem(request):
	if request.method == 'GET':
		print request.method
		return render(request, 'tycoon/codeToItem.html')
	
	elif request.method == 'POST':
		res_code = request.POST.get('codeToItem', False)
		if res_code == False:
			message = 'Wrong Code'
		else:
			try:
				code_to_item = CodeToItem.objects.get(code=res_code)
				if code_to_item.is_used == True:
					message = 'Already uesed!'
				else:
					my_avatar = Avatar.objects.get(pk=1)
					c = Contain(name=my_avatar, item=code_to_item.item)
					c.save()
					message = code_to_item.item.name
					code_to_item.is_used = True
					code_to_item.save()
					my_avatar.item_list.add(code_to_item.item)
				print message
			except:
				message = 'Wrong Code'
				print message
	 	return render(request, 'tycoon/codeToItem.html', { 'message': message })	

def mission(request):
	return render(request, 'tycoon/mission.html')

def itemBook(request):
	item_list = Item.objects.all()
	item_name_list = [item_list[i].name for i in range(len(item_list))]
	own_list = Avatar.objects.get(pk=1).item_list.all()
	own_name_list = [own_list[i].name for i in range(len(own_list))]
	c = [item_name_list[i] in own_name_list for i in range(len(item_list))]
	item_list = zip(item_list, c)
	return render(request, 'tycoon/itemBook.html', { 'item_list': item_list})

def use(request):
	avatar = Avatar.objects.get(pk=1)
	class1_list = Contain.objects.filter(name__name__startswith='chaeyong').order_by('item')
	return render(request, 'tycoon/use.html', {'avatar': avatar, 'clist': class1_list})

