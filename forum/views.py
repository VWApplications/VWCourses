from django.shortcuts import render
from django.views.generic import ListView
from .models import Topic


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
    return queryset

  def get_context_data(self):
    context = super(ForumView, self).get_context_data()
    context['tags'] = Topic.tags.all()
    return context
