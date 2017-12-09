from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime as datetime

# Create your models here.
class Post(models.Model):
	poster = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	date_posted = models.DateField()
	content = models.CharField(max_length=1000)

	def __str__(self):
		return self.title
	def set_poster(self,poster):
		self.poster = poster

class Comment(models.Model):
	poster = models.CharField(max_length=100)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	content = models.CharField(max_length=1000)
	date_posted = models.DateTimeField()

	def __str__(self):
		return self.id
	def set_poster(self,poster):
		self.poster = poster