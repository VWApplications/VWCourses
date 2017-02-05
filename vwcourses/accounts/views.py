from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.decorators import login_required
from vwcourses.courses.models import Enrollment
from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset


def register(request):
  template = 'accounts/register.html'
  form = RegisterForm(request.POST or None)
  if form.is_valid():
    user = form.save()
    user = authenticate(
      username=user.username,
      password=form.cleaned_data['password1']
    )
    login(request, user)
    return redirect('core:home')
  context = {
    'form': form,
  }
  return render(request, template, context)


def reset_password(request):
  template = 'accounts/reset_password.html'
  form = PasswordResetForm(request.POST or None)
  context = {}
  if form.is_valid():
    form.save()
    context['success'] = True
  context['form'] = form
  return render(request, template, context)


def reset_password_confirm(request, key):
  template = 'accounts/reset_password_confirm.html'
  context = {}
  reset = get_object_or_404(PasswordReset, key=key)
  form = SetPasswordForm(user=reset.user, data=request.POST or None)
  if form.is_valid():
    form.save()
    context['success'] = True
  context['form'] = form
  return render(request, template, context)


@login_required
def profile(request):
  template = 'accounts/profile.html'
  context = {}
  return render(request, template, context)


@login_required
def edit(request):
  template = 'accounts/edit.html'
  context = {}
  form = EditAccountForm(request.POST or None, instance=request.user)
  if form.is_valid():
    form.save()
    messages.success(request, 'Os dados da sua conta foram alterados com sucesso')
    return redirect('accounts:profile')
  context['form'] = form
  return render(request, template, context)


@login_required
def edit_password(request):
  template = 'accounts/edit_password.html'
  context = {}
  form = PasswordChangeForm(data=request.POST or None, user=request.user)
  if form.is_valid():
    form.save()
    messages.success(request, 'A senha foi alterada com sucesso')
    return redirect('accounts:login')
  context['form'] = form
  return render(request, template, context)
