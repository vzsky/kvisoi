from django.contrib import admin
from .models import Task, Submission, TaskConfig

admin.site.register(Task)
admin.site.register(TaskConfig)
admin.site.register(Submission)