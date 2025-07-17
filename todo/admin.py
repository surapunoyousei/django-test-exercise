from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_closed', 'created_at')
    search_fields = ('title',)
    list_filter = ('is_closed',)

admin.site.register(Task, TaskAdmin)