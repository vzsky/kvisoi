from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  url(r'^id/(?P<id>[0-9]+)$', views.user, name='user-byid'),
  url(r'^me/$', views.me, name='myprofile'),
  url(r'^register/$', views.register, name='user-register'),
  url(r'^login/$', auth_views.LoginView.as_view(template_name="users/login.html"), name='user-login'),
  url(r'^logout/$', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='user-logout'),
]