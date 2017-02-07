from django.conf.urls import url
from . import views

app_name = 'forum'
urlpatterns = [
  url(r'^$', views.ForumView.as_view(), name="index")
]
