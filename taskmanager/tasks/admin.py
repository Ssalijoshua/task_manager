from django.contrib import admin
from tasks.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "status", "owner", "created_at", "updated_at")
    list_filter = ("status",)
    actions = ['mark_archived']

    def mark_archived(self, request, queryset):
        queryset.update(status='ARCHIVED')

    mark_archived.short_description = 'Mark selected tasks as archived'

    def has_change_permission(self, request, obj=None):
        return request.user.has_perm('tasks.change_task')

    def has_add_permission(self, request):
        return request.user.has_perm('tasks.add_task')

    def has_delete_permission(self, request, obj=None):
        return request.user.has_perm('tasks.delete_task')

admin.site.register(Task, TaskAdmin)
