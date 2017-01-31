from django.contrib.auth.models import User
from .models import Avatar

def pass_nav_all_users(request):
	user = request.user.id
	users = User.objects.filter(username__startswith='class')
	users_id = [ users[i].id for i in range(len(users))]
	avatars = [ Avatar.objects.get(host=users[i].id).name for i in range(len(users))]
	all_users = zip(users_id, avatars)
	return { "login_user": user, "all_users": all_users }
