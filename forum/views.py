import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.contrib import messages
from django.http import HttpResponse
from .models import Topic, Reply
from .forms import ReplyForm


class ForumView(ListView):
  paginate_by = 2
  template_name = 'forum/index.html'

  def get_queryset(self):
    queryset = Topic.objects.all()
    order = self.request.GET.get('order', 'recents')
    if order == 'views':
      queryset = queryset.order_by('-views')
    elif order == 'answers':
      queryset = queryset.order_by('-answers')
    tag = self.kwargs.get('tag', '')
    if tag:
      queryset = queryset.filter(tags__slug__icontains=tag)
    return queryset

  def get_context_data(self):
    context = super(ForumView, self).get_context_data()
    context['tags'] = Topic.tags.all()
    return context


class TopicView(DetailView):
  model = Topic
  template_name = 'forum/topic.html'

  def get(self, *args, **kwargs):
    response = super(TopicView, self).get(self.request, *args, **kwargs)
    if not self.request.user.is_authenticated() or (self.object.author != self.request.user):
      self.object.views = self.object.views + 1
      self.object.save()
    return response

  def get_context_data(self, **kwargs):
    context = super(TopicView, self).get_context_data(**kwargs)
    context['tags'] = Topic.tags.all()
    context['form'] = ReplyForm(self.request.POST or None)
    return context

  def post(self, request, *args, **kwargs):
    if not self.request.user.is_authenticated():
      messages.error(self.request, 'Você não tem permissão para responde ao tópico, precisa está logado')
      return redirect(self.request.path)
    self.object = self.get_object()
    context = self.get_context_data(object=self.object)
    form = context['form']
    if form.is_valid():
      reply = form.save(commit=False)
      reply.topic = self.object
      reply.author = self.request.user
      reply.save()
      messages.success(self.request, 'A sua resposta foi enviada com sucesso')
      context['form'] = ReplyForm()
    return self.render_to_response(context)


class ReplyCorrectView(View):

  correct = True

  def get(self, request, reply_pk):
    reply = get_object_or_404(Reply, pk=reply_pk, topic__author=request.user)
    reply.correct = self.correct
    reply.save()
    messages.success(self.request, 'Resposta atualizada com sucesso')
    return redirect(reply.topic.get_absolute_url())
