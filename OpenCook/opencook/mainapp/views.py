from django.shortcuts import render, redirect
from recipe.models import Recipe
from datetime import timedelta, datetime

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth

# Create your views here.

def get_index(request):
	title = 'OpenCook'
	recipes = Recipe.objects.all()
	response = render(request, 'index.html', locals())
	#response.set_cookie(key='name', value='hi i am a cookie', expires=datetime.now() + timedelta(days=30))
	return response


def get_signup(request):
	#print(request.session['age'])
	return render(request, 'signup.html')


def post_signup(request):
	username = request.POST['username']
	email = request.POST['email']
	password = request.POST['password']

	user = User.objects.create_user(username, email, password)
	if user:  #如果user不是null
		return redirect('/', locals())
	else:	
		redirect('/signup', locals()) 
		
def post_logout(request):
	auth.logout(request)
	return redirect('/')


def post_login(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return redirect('/', locals())
	else:
		return redirect('/', locals())	














