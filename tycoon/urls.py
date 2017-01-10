from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	url(r'^combination', views.combination, name='combination'),
	url(r'^$', views.home, name='home'),
]
