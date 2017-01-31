from django.contrib.auth.models import User

def pass_nav_all_users(request):
	user = request.user.id
	users = User.objects.filter(username__startswith='class')
	return { "login_user": user, "all_users": users }