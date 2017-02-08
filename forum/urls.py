from django.conf.urls import url
from . import views

app_name = 'forum'
urlpatterns = [
  url(r'^$', views.ForumView.as_view(), name="index"),
  url(r'^tag/(?P<tag>[\w_-]+)/$', views.ForumView.as_view(), name="index_tag"),
  url(r'^(?P<slug>[\w_-]+)/$', views.TopicView.as_view(), name="topic"),
  url(r'^respostas/(?P<reply_pk>\d+)/correta/$', views.ReplyCorrectView.as_view(), name="reply_correct"),
  url(r'^respostas/(?P<reply_pk>\d+)/incorreta/$', views.ReplyCorrectView.as_view(correct=False), name="reply_incorrect"),
]
