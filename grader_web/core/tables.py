import django_tables2 as tables
from django_tables2.utils import A
from .models import Submission, Task
from django.utils.safestring import mark_safe

class SubmissionTable(tables.Table):
  id = tables.Column(orderable=False)
  task = tables.LinkColumn('core-task', args=[A('task.id')], orderable=False)
  owner = tables.Column(orderable=False)
  lang = tables.Column(orderable=False)
  status = tables.Column(orderable=False)
  score = tables.Column(orderable=False)
  view = tables.LinkColumn('core-submission', text="view", args=[A('id')], orderable=False)
  class Meta:
    model = Submission
    template_name = "django_tables2/bootstrap.html"
    exclude = ('code', 'timeUsed', 'memoryUsed')

class TaskTable(tables.Table):
  id = tables.Column(orderable=False)
  title = tables.LinkColumn('core-task', args=[A('id')], orderable=False)
  author = tables.Column(orderable=False)
  class Meta:
    model = Task
    template_name = "django_tables2/bootstrap.html"
    # exclude = ('','')
