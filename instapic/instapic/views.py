from django.shortcuts import render, redirect
from .models import User
from .forms import *
from django.contrib.auth import authenticate, login, logout as dlogout

def ajaxsignup(request):
	ajax = AjaxSignUp(request.POST)
	context = {'ajax_output': ajax.output() }
	return render(request, 'ajax.html', context)

def ajaxlogin(request):
	ajax = AjaxLogin(request.POST)
	logged_in_user, output = ajax.validate()
	if logged_in_user != None:
		login(request, logged_in_user)
	context = {'ajax_output': output}
	return render(request, 'ajax.html', context)

def signup(request):
    context = {}
    return render(request, 'sign-up.html', context)

def home(request):
	context = {}
	if request.is_authenticated:
		u = User.objects.filter(username=request.user.username)[0]
		if u.profilepic == "":
			u.profilepic = "static/assets/img/default.png"
		context = { 'user': request.user, 'ProfilePic': u.profilepic}
		return render(request, 'logged-in-index.html', context)

def index(request):
    context = {}
    return render(request, 'index.html', context)

