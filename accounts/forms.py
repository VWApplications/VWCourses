from django import forms
from django.contrib.auth import get_user_model
from vwcourses.core.utils import generate_hash_key
from vwcourses.core.mail import send_email_template
from .models import PasswordReset

User = get_user_model()


class RegisterForm(forms.ModelForm):
  password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Confirmação de senha', widget=forms.PasswordInput)

  def clean_password2(self):
    password1 = self.cleaned_data.get('password1')
    password2 = self.cleaned_data.get('password2')
    if password1 and password2 and password1 != password2:
      raise forms.ValidationError('Confirmação de senha incorreta')
    return password2

  def save(self, commit=True):
    user = super(RegisterForm, self).save(commit=False)
    user.set_password(self.cleaned_data['password1'])
    if commit:
      user.save()
    return user

  class Meta:
    model = User
    fields = ['username', 'email']


class EditAccountForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'name']


class PasswordResetForm(forms.Form):
  email = forms.EmailField(label='E-mail')

  def clean_email(self):
    email = self.cleaned_data['email']
    if User.objects.filter(email=email).exists():
      return email
    raise forms.ValidationError('Nenhum usuário encontrado com esse email')

  def save(self):
    user = User.objects.get(email=self.cleaned_data['email'])
    key = generate_hash_key(user.username)
    reset_password = PasswordReset(user=user, key=key)
    reset_password.save()
    template = 'accounts/reset_password_email.html'
    subject = 'Solicitando nova senha'
    context = {'reset_password': reset_password}
    send_email_template(subject, template, context, [user.email])
