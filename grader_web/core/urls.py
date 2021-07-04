from django.conf.urls import url
from . import views

# OPEN URLS
urlpatterns = [
  url(r'^$', views.home, name='core-home'),
  url(r'^task/(?P<id>[a-zA-Z0-9-_]+)$', views.task, name='core-task'),
  url(r'^tasks$', views.tasks, name='core-tasks'),
  url(r'^submission/(?P<id>[0-9]+)$', views.submission, name='core-submission'),
  url(r'^submissions/$', views.submissions, name='core-submissions'),
  url(r'^submit/$', views.submit, name='core-submit'),
]
