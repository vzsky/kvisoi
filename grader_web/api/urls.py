from django.conf.urls import url
from . import views

# OPEN URLS
urlpatterns = [
  url(r'^apistatus$', views.apistatus, name='api-home'),
  url(r'^message$', views.message, name='api-message'),
  url(r'^group$', views.group, name='api-group'),
]