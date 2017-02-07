from django.conf.urls import url
from . import views

app_name = 'courses'
urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^(?P<course_slug>[\w_-]+)/$', views.details, name='details'),
  url(r'^(?P<course_slug>[\w_-]+)/inscricao/$', views.enrollment, name='enrollment'),
  url(r'^(?P<course_slug>[\w_-]+)/cancelar-inscricao/$', views.cancel_enrollment, name='cancel_enrollment'),
  url(r'^(?P<course_slug>[\w_-]+)/anuncios/$', views.announcements, name='announcements'),
  url(r'^(?P<course_slug>[\w_-]+)/anuncios/(?P<announcement_id>[0-9]+)/$', views.show_announcement, name='show_announcement'),
  url(r'^(?P<course_slug>[\w_-]+)/aulas/$', views.lessons, name='lessons'),
  url(r'^(?P<course_slug>[\w_-]+)/aulas/(?P<lesson_id>[0-9]+)/$', views.lesson, name='lesson'),
  url(r'^(?P<course_slug>[\w_-]+)/materiais/(?P<material_id>[0-9]+)/$', views.material, name='material'),
  url(r'^(?P<course_slug>[\w_-]+)/informacoes/$', views.information, name='information'),
]
