from django.shortcuts import get_object_or_404,render,redirect,reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from . import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

#from .models import *
# Create your views here.
class LoginFormView(generic.View):
	template_name = 'registrations/login.html'
	form_class = forms.LoginForm
	def get(self, request):
		if request.user.is_authenticated:
			return redirect(reverse('userlist'))
		form = self.form_class(None)
		return render(request,self.template_name, {'form':form})

	def post(self, request):
		if request.user.is_authenticated:
			return redirect(reverse('home'))
		form = self.form_class(None)
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect(reverse('home'))
		return render(request,self.template_name,{"form":form})

class RegisterFormView(generic.View):
	template_name = 'registrations/register.html'
	form_class = forms.RegisterForm
	def get(self, request):
		if request.user.is_authenticated:
			return redirect(reverse('home'))
		form = self.form_class(None)
		return render(request,self.template_name, {'form':form})

	def post(self, request):
		if request.user.is_authenticated:
			return redirect(reverse('home'))
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			login(request,user)
			return redirect(reverse('home'))
		return render(request,self.template_name,{"form":form})

class ViewPostView(generic.DetailView):
	template_name = 'viewpost.html'
	# model = Comment
	def get(self, request,pk):
		post = Post.objects.get(pk=pk)
		mycomments = Comment.objects.filter(post=post, poster=request.user)
		comments = Comment.objects.filter(post=post)
		comments = comments.exclude(poster=request.user)
		return render(request,self.template_name,{'mycomments': mycomments, 'comments':comments,'post':post})

def HomeView(request):
	if request.user.is_authenticated:
		return render(request, 'home.html', {'posts': Post.objects.exclude(poster=request.user)})
	else:
		return render(request, 'home.html', {'posts': Post.objects.all()})

def logoutpage(request):
	logout(request)
	return redirect(reverse('home'))

def SearchPost(request):
	substring = request.POST.get('substring')
	subtitle = Post.objects.filter(title__contains=substring)
	subcontent = Post.objects.filter(content__contains=substring)
	return render(request, 'searchpost.html', {'subtitle': subtitle, 'subcontent': subcontent})

@login_required()
def SaveComment(request):
	content = request.POST.get('comment')
	pk = request.POST.get('pk')
	post = Post.objects.get(id=pk)
	date_posted = datetime.datetime.now()
	comment = Comment.objects.create(poster=request.user, post=post, content=content, date_posted=date_posted)
	mycomments = Comment.objects.filter(post=post, poster=request.user)
	comments = Comment.objects.filter(post=post)
	comments = comments.exclude(poster=request.user)
	return render(request, 'viewpost.html', {'mycomments': mycomments, 'comments':comments,'post':post})

@login_required()
def MyPosts(request):
	posts = Post.objects.filter(poster=request.user)
	empty = True
	if posts:
		empty = False
	return render(request, 'myposts.html', {'posts': posts, 'empty': empty})

@login_required()
def CreatePost(request):
	return render(request, 'createPost.html')

@login_required()
def SavePost(request):
	title = request.POST.get('title')
	content = request.POST.get('content')
	date_posted = datetime.datetime.now()
	Post.objects.create(poster=request.user, title=title, date_posted=date_posted, content=content)
	posts = Post.objects.filter(poster=request.user)
	empty = True
	if posts:
		empty = False
	return render(request, 'myposts.html', {'posts': posts, 'empty': empty})

@login_required()
def PostDelete(request, pid):
	Post.objects.get(id=pid).delete()
	posts = Post.objects.filter(poster=request.user)
	empty = True
	if posts:
		empty = False
	return render(request, 'myposts.html', {'posts': posts, 'empty': empty})

@login_required()
def CommentDelete(request, pid, cid):
	Comment.objects.get(id=cid).delete()
	post = Post.objects.get(id=pid)
	mycomments = Comment.objects.filter(post=post, poster=request.user)
	comments = Comment.objects.filter(post=post)
	comments = comments.exclude(poster=request.user)
	return render(request, 'viewpost.html', {'mycomments': mycomments, 'comments':comments,'post':post})

@login_required()
def MyAccount(request):
	postcount = len(Post.objects.filter(poster=request.user))
	commentcount = len(Comment.objects.filter(poster=request.user))	
	return render(request, 'myaccount.html', {'user': request.user, 'postcount': postcount, 'commentcount': commentcount})