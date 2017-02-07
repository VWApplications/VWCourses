from django.contrib import admin
from .models import Topic, Reply

class TopicAdmin(admin.ModelAdmin):
  list_display = ['title', 'author', 'created_at', 'updated_at']
  search_fields = ['title', 'author__email', 'body']

class ReplyAdmin(admin.ModelAdmin):
  list_display = ['topic', 'author', 'created_at', 'updated_at']
  search_fields = ['topic__title', 'author__email', 'body']


admin.site.register(Topic, TopicAdmin)
admin.site.register(Reply, ReplyAdmin)
