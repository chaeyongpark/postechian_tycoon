from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	url(r'^avatar', views.avatar, name='avatar'),
	url(r'^codeToItem', views.codeToItem, name='codeToItem'),
	url(r'^use', views.use, name='use'),
	url(r'^combination', views.combination, name='combination'),
	url(r'^itemBook', views.itemBook, name='itemBook'),
	url(r'^mission', views.mission, name='mission'),
	url(r'^', views.home, name='home'),
]
