#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Map, Close, Item, Avatar, Contain, Combination, CodeToItem, CombinationContain, Mission
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):
	is_closed = Close.objects.get(id=1).is_closed;

	if is_closed :
		return render(request, 'tycoon/close.html')

	return render(request, 'tycoon/home.html')

@login_required(login_url='/login/')
def map(request):
	image = Map.objects.get(id=1).image;

	return render(request, 'tycoon/map.html', {'image': image})

@login_required(login_url='/login/')
def combination(request):
	is_closed = Close.objects.get(id=1).is_closed;

	if is_closed :
		return render(request, 'tycoon/close.html')

	avatar = Avatar.objects.get(host=request.user.id)
	own_list = Contain.objects.filter(name__name__startswith=avatar.name).order_by('item')

	if request.method == 'GET':
		return render(request, 'tycoon/combination.html', {'avatar': avatar, 'clist': own_list})
	
	elif request.method == 'POST':

		# Check 2 contains exist
		try:
			left_item_contain = Contain.objects.get(id=request.POST.get('left', False))
			right_item_contain = Contain.objects.get(id=request.POST.get('right', False))
		except:
			print "Contains don't exist"
			return render(request, 'tycoon/combination.html', {'avatar': avatar, 'clist': own_list})

		# Check 2 contains belong to user
		if left_item_contain.name == avatar and right_item_contain.name == avatar:
			pass
		else:
			print "Contains don't belong to user"
			return render(request, 'tycoon/combination.html', {'avatar': avatar, 'clist': own_list})

		# Get item from contains
		left_item = left_item_contain.item
		right_item = right_item_contain.item

		# Check if combination exists
		try:
			comb = Combination.objects.get(item1__name=left_item.name, item2__name=right_item.name)
		except:
			try:
				comb = Combination.objects.get(item2__name=left_item.name, item1__name=right_item.name)
			except:
				# Combination doesn't exist s.t. return nitem.id as 0
				print "Combination doesn't exist"
				return JsonResponse({'nitem': {'id': 0, 'url': 'null', 'explanataion': 'Combination does not exist' }})
		
		# Check if this request for actual combination command
		if request.POST.get('real', None) == "true":
			print "User actually requested combination"
			left_item_contain.delete()
			right_item_contain.delete()
			new_item = Item.objects.get(id=comb.new_item.id)
			avatar.item_list.add(new_item)
			new_contain = Contain(name=avatar, item=new_item)
			new_contain.save()
			avatar.strength += comb.strength_b
			avatar.intelligence += comb.intelligence_b
			avatar.charm += comb.charm_b
			avatar.surplus += comb.surplus_b
			avatar.luck += comb.luck_b
			avatar.save()

		# Check if this combination was used by user
		try:
			CombinationContain.objects.get(name=avatar, combination=comb)
		except:
			new_combination_contain = CombinationContain(name=avatar, combination=comb)
			new_combination_contain.save()
			before = False;
		else:
			before = True;

		# Return the results
		return JsonResponse({'nitem': {
				'id': comb.new_item.id, 
				'url': comb.new_item.icon.url, 
				'name': comb.new_item.name,
				'explanation': comb.explanation }, 
			'before': before})
	

@login_required(login_url='/login/')
def avatar(request, id=None):
	is_closed = Close.objects.get(id=1).is_closed;

	if is_closed :
		return render(request, 'tycoon/close.html')

	if id == None :
		id = request.user.id
	avatar = Avatar.objects.get(host=id)
	maximum = max([avatar.strength, avatar.intelligence, avatar.luck, avatar.surplus, avatar.charm]) / 5 * 5 + 5
	return render(request, 'tycoon/avatar.html', {'avatar': avatar, 'maximum': maximum })

@login_required(login_url='/login/')
def codeToItem(request):
	is_closed = Close.objects.get(id=1).is_closed;

	if is_closed :
		return render(request, 'tycoon/close.html')

	if request.method == 'GET':
		return render(request, 'tycoon/codeToItem.html')
	
	elif request.method == 'POST':
		res_code = request.POST.get('codeToItem', False)
		if res_code == False:
			message = 'wrong'
			item_img_url = '/static/tycoon/wrong.png'
		else:
			try:
				code_to_item = CodeToItem.objects.get(code=res_code)
				if code_to_item.is_used == True:
					message = 'used'
					item_img_url = '/static/tycoon/used.png'
				else:
					avatar = Avatar.objects.get(host=request.user.id)
					c = Contain(name=avatar, item=code_to_item.item)				
					c.save()
					item_img_url = code_to_item.item.icon.url
					message =code_to_item.item.name
					code_to_item.is_used = True
					code_to_item.save()
					avatar.item_list.add(code_to_item.item)
			except:
				message = 'wrong'
				item_img_url = '/static/tycoon/wrong.png'
		
	 	return JsonResponse({'item_img': item_img_url, 'message': message})

def mission(request):
	is_closed = Close.objects.get(id=1).is_closed;

	if is_closed :
		return render(request, 'tycoon/close.html')

	mission_list = Mission.objects.all()
	avatar = Avatar.objects.get(host=request.user.id)
	mission_clear_list = [mission_list[i] in avatar.mission_list.all() for i in range(len(mission_list))]
	result = zip(mission_list, mission_clear_list)
	return render(request, 'tycoon/mission.html', { 'result': result })

@login_required(login_url='/login/')
def itemBook(request):
	is_closed = Close.objects.get(id=1).is_closed;

	if is_closed :
		return render(request, 'tycoon/close.html')

	item_list = Item.objects.all()
	avatar = Avatar.objects.get(host=request.user.id)
	item_name_list = [item_list[i].name for i in range(len(item_list)) if not item_list[i].event]
	own_list = avatar.item_list.all()
	own_name_list = [own_list[i].name for i in range(len(own_list))]
	c = [item_name_list[i] in own_name_list for i in range(len(item_name_list))]
	item_list = zip(item_list, c)

	#Combination Contain list
	comb_list = CombinationContain.objects.filter(name__name__startswith=avatar.name).order_by('combination')
	return render(request, 'tycoon/itemBook.html', { 'item_list': item_list, 'comb_list': comb_list })

@login_required(login_url='/login/')
def use(request):
	is_closed = Close.objects.get(id=1).is_closed;

	if is_closed :
		return render(request, 'tycoon/close.html')

	avatar = Avatar.objects.get(host=request.user.id)

	if request.method == 'POST':
		cid = request.POST.get('contains_id', False)

		try:
			contain = Contain.objects.get(id=cid)
			contain.delete()

			avatar.strength += contain.item.strength
			avatar.intelligence += contain.item.intelligence
			avatar.charm += contain.item.charm
			avatar.surplus += contain.item.surplus
			avatar.luck += contain.item.luck
			avatar.save()

		except:
			pass
	
	own_list = Contain.objects.filter(name__name__startswith=avatar.name).order_by('item')
	maximum = max([avatar.strength, avatar.intelligence, avatar.luck, avatar.surplus, avatar.charm]) / 5 * 5 + 5
	return render(request, 'tycoon/use.html', {'avatar': avatar, 'clist': own_list, 'maximum': maximum })
