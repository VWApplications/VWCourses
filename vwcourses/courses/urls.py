from django.conf.urls import url
from . import views

app_name = 'courses'
urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^(?P<course_slug>[\w_-]+)/$', views.details, name='details'),
]
