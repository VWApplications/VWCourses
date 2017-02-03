from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core import validators
from django.conf import settings
import re

class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField('Nome de Usuário', max_length=30, unique=True,
    help_text='O nome de usuário é um campo obrigatório de até 30 caracteres ou menos, entre eles letras e números',
    validators = [
      validators.RegexValidator(
        re.compile('^[\w.@-_]+$'),
        'O nome de usuário só pode conter letras, números e simbolos como @.-_',
        'invalid'
      )
    ]
  )
  email = models.EmailField('E-mail', unique=True)
  name = models.CharField('Nome', max_length=100, blank=True)
  is_active = models.BooleanField('Está Ativo?', blank=True, default=True)
  is_staff = models.BooleanField('É administrador?', blank=True, default=False)
  date_joined = models.DateTimeField('Data de Cadastro', auto_now_add=True)

  objects = UserManager()

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['email']

  def __str__(self):
    return self.name or self.username

  def get_short_name(self):
    return self.username

  def get_full_name(self):
    return str(self)

  class Meta:
    verbose_name = 'Usuário'
    verbose_name_plural = 'Usuários'

class PasswordReset(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='password_resets')
  key = models.CharField('Chave', max_length=100, unique=True)
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  confirmed = models.BooleanField('Confirmado?', default=False, blank=True)

  def __str__(self):
    return '{0} - {1}'.format(self.user, self.created_at)

  class Meta:
    verbose_name = 'Nova senha'
    verbose_name_plural = 'Novas senhas'
    ordering = ['-created_at']
