from django.conf.urls import url
from . import views

app_name = 'core'
urlpatterns = [
  # home/
  url(r'^$', views.home, name='home'),
  url(r'^contato/$', views.contact, name='contact'),
]
