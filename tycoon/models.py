from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.db import models

@python_2_unicode_compatible
class Title(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Item(models.Model):
	name = models.CharField(max_length=20)
	icon = models.ImageField(upload_to='images/icon/', default='static/tycoon/blank.png') 
	strength = models.IntegerField(default=0)
	intelligence = models.IntegerField(default=0)
	charm = models.IntegerField(default=0)
	surplus = models.IntegerField(default=0)
	luck = models.IntegerField(default=0)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class CodeToItem(models.Model):
	code = models.CharField(max_length=20)
	item = models.ForeignKey(Item)
	is_used = models.BooleanField(default=False)
	explanation = models.CharField(max_length=30, default='Explanation')

	def __str__(self):
		return self.code + " == " + self.item.name

@python_2_unicode_compatible
class Combination(models.Model):
	item1 = models.ForeignKey(Item, related_name='item1')
	item2 = models.ForeignKey(Item, related_name='item2')
	new_item = models.ForeignKey(Item, related_name='new_item') 
	explanation = models.CharField(max_length=40, default='Explanation')

	def __str__(self):
		return self.new_item.name + " = " + self.item1.name + " + " + self.item2.name

@python_2_unicode_compatible
class Avatar(models.Model):
	host = models.ForeignKey(User, default=1)
	name = models.CharField(max_length=20, default='chaeyong')
	image_f = models.ImageField(upload_to='images/avatar/', default='images/avatar/default.png')
	image_b = models.ImageField(upload_to='images/avatar/', default='images/avatar/default.png')
	strength = models.IntegerField(default=0)
	intelligence = models.IntegerField(default=0)
	charm = models.IntegerField(default=0)
	surplus = models.IntegerField(default=0)
	luck = models.IntegerField(default=0)
	cur_title = models.ForeignKey(Title, related_name='cur_title', null=True, blank=True)
	title_list = models.ManyToManyField(Title, related_name='title_list', blank=True)
	item_list = models.ManyToManyField(Item, blank=True, db_index=True)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Contain(models.Model):
	name = models.ForeignKey(Avatar, db_index=True)
	item = models.ForeignKey(Item)

	def __str__(self):
		return self.name.name + " " + self.item.name

@python_2_unicode_compatible
class CombinationContain(models.Model):
	name = models.ForeignKey (Avatar, db_index=True)
	combination = models.ForeignKey(Combination)

	def __str__(self):
		return self.name.name + " has " + self.combination.new_item.name
