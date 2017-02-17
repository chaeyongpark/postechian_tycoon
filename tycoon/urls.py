from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	url(r'^home/$', views.avatar, name='home'),
	url(r'^avatar/(?P<id>[0-9]+)/$', views.avatar, name='avatar'),
	url(r'^codeToItem/$', views.codeToItem, name='codeToItem'),
	url(r'^use/$', views.use, name='use'),
	url(r'^combination/$', views.combination, name='combination'),
	url(r'^itemBook/$', views.itemBook, name='itemBook'),
	url(r'^mission/$', views.mission, name='mission'),
	url(r'^map/$', views.map, name='map'),
	url(r'^ranking/$', views.ranking, name='ranking'),
	url(r'^lab/$', views.lab, name='lab'),
	url(r'^start/$', views.maze101, name='start'),
	url(r'^2017FreshmanOrientationPreparationCommitee/$', views.maze102, name='2017FreshmanOrientationPreparationCommitee'),
	url(r'^2017FreshmanOrientationPreparationCommittee/$', views.maze102, name='2017FreshmanOrientationPreparationCommittee'),
	url(r'^17OT/$', views.maze103, name='17OT'),
	url(r'^beginning2/$', views.maze201, name='beginning2'),
	url(r'^ILoveYou/$', views.maze202, name='ILoveYou'),
	url(r'^8888888/$', views.maze203, name='8888888'),
	url(r'^3he8ht/$', views.maze204, name='3he8ht'),
]