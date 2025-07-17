from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed', 'posted_at', 'priority')
    search_fields = ('title', )
    list_filter = ('completed', 'priority')


admin.site.register(Task, TaskAdmin)
