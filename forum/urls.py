from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
	url(r'^myposts/createPost/$', views.CreatePost, name='createpost'),
	url(r'^myposts/createPost/post_submitted/$', views.SavePost, name='save_post'),
	url(r'^home/search_post/', views.SearchPost, name='searchpost'),
	url(r'^$', RedirectView.as_view(permanent=False,pattern_name='home')),
	url(r'^login/$', views.LoginFormView.as_view(), name='login'),
	url(r'^logout/$', views.logoutpage, name='logout'),
	url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
	url(r'^home/$', views.HomeView, name='home'),
	url(r'^home/comment_submitted/$', views.SaveComment, name='save_comment'),
	url(r'^myaccount/$', views.MyAccount, name='myaccount'),
	url(r'^myposts/$', views.MyPosts, name='myposts'),
	url(r'^myposts/(?P<pid>\d+)/post_deleted/$', views.PostDelete, name='deletepost'),
	url(r'^home/(?P<pid>[^\s]+)/(?P<cid>[^\s]+)/comment_deleted/$', views.CommentDelete, name='deletecomment'),
	url(r'^home/(?P<pk>[^\s]+)/', views.ViewPostView.as_view(), name='viewpost'),
]