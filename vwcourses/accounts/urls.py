from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

app_name = 'accounts'
urlpatterns = [
  url(r'^$', views.profile, name="profile"),
  url(r'^entrar/$', login, {'template_name': 'accounts/login.html'}, name="login"),
  url(r'^sair/$', logout, {'next_page': 'core:home'}, name="logout"),
  url(r'^cadastrar/$', views.register, name="register"),
  url(r'^editar/$', views.edit, name="edit"),
  url(r'^editar-senha/$', views.edit_password, name="edit_password"),
  url(r'^resetar-senha/$', views.reset_password, name="reset_password"),
  url(r'^confirmar-nova-senha/(?P<key>\w+)/$', views.reset_password_confirm, name="reset_password_confirm")
]
