from django.contrib import admin
from .models import Topic, Reply

class TopicAdmin(admin.ModelAdmin):
  fields = ['title', 'slug', 'author', 'body', 'tags']
  list_display = ['title', 'author', 'created_at', 'updated_at']
  search_fields = ['title', 'author__email', 'body']
  prepopulated_fields = {'slug': ('title',)}

class ReplyAdmin(admin.ModelAdmin):
  list_display = ['topic', 'author', 'correct', 'created_at', 'updated_at']
  search_fields = ['topic__title', 'author__email', 'body']


admin.site.register(Topic, TopicAdmin)
admin.site.register(Reply, ReplyAdmin)
