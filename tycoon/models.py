from __future__ import unicode_literals
from django.db import models

class User(models.Model):
	#user_id = models.CharField(max_length=20)
	user_password = models.CharField(max_length=20)
	is_pw_changed = models.BooleanField(default=False)

class Title(models.Model):
	name = models.CharField(max_length=20)

class Item(models.Model):
	name = models.CharField(max_length=20)
	icon = models.ImageField(upload_to="images/icon") 
	strength = models.IntegerField(default=0)
	intelligence = models.IntegerField(default=0)
	charm = models.IntegerField(default=0)
	surplus = models.IntegerField(default=0)
	luck = models.IntegerField(default=0)
	explanation = models.CharField(max_length=20)

class CodeToItem(models.Model):
	code = models.CharField(max_length=20)
	item = models.ForeignKey(Item)

class Combination(models.Model):
	item1 = models.ForeignKey(Item, related_name='item1')
	item2 = models.ForeignKey(Item, related_name='item2')
	new_item = models.ForeignKey(Item, related_name='new_item') 

class Avatar(models.Model):
	image = models.ImageField(upload_to="images/avatar")
	strength = models.IntegerField(default=0)
	intelligence = models.IntegerField(default=0)
	charm = models.IntegerField(default=0)
	surplus = models.IntegerField(default=0)
	luck = models.IntegerField(default=0)
	cur_title = models.ForeignKey(Title)
