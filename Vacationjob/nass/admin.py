from django.contrib import admin
from .models import Task, Wallet ,TaskUserAssignment

admin.site.register(Task)
admin.site.register(Wallet)

@admin.register(TaskUserAssignment)
class TaskUserAssignmentAdmin(admin.ModelAdmin):
    # Columns displayed in the admin panel list view
    list_display = ['task', 'user', 'clicked_at', 'proof_screenshot', 'submission_status']
    
    # Filters to narrow down the displayed records
    list_filter = ['task', 'clicked_at', 'submission_status']
    
    # Enable searching for specific users or tasks
    search_fields = ['user__username', 'task__title']
    
    # Make clicked_at and submission_status fields readonly
    # readonly_fields = ['clicked_at', 'submission_status']
