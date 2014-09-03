from django.contrib import admin
from sites.models import Task

class TaskAdmin(admin.ModelAdmin):
	list_display = ('start_url', 'end_url', )


admin.site.register(Task, TaskAdmin)
