from django import forms
from django.contrib.auth.models import User
from .models import *
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
    	model = User
    	fields = [
    		'username',
    		'password'
    	]

class RegisterForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
	class Meta:
		model = User
		fields = [
			'username',
			'password'
		]	
	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")

		if password != confirm_password:
			raise forms.ValidationError(
			"Passwords do not match"
			)

class CreatePostForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput())
	content = forms.CharField(widget=forms.TextInput())
	class Meta:
		model = Post
		fields = [
			'title',
			'content'
		]
