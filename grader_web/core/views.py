from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, Submission
from .forms import SubmissionForm
from django.contrib.auth.decorators import login_required
from grader_web.settings import PENDING_STATUS, API_URL, API_SEND_PORT
import requests, re
from .tables import SubmissionTable, TaskTable

def home (req) :
  return render(req, 'core/home.html')

# should do pagination
def tasks (req) : 
  return render(req, 'core/tasks.html', {
    'table' : TaskTable(Task.objects.all())
  })

def task (req, id) :
  return render(req, 'core/task.html', {
    'task' : Task.objects.get(id=id)
  })

# should do pagination
def submissions (req) :
  return render(req, 'core/submissions.html', {
    'table' : SubmissionTable(Submission.objects.all())
  })

def submission (req, id) : 
  return render(req, 'core/submission.html', {
    'submission' : Submission.objects.get(id=id)
  })

@login_required
def submit (req) :
  if req.method == 'POST' :
    form = SubmissionForm(req.POST)
    if form.is_valid() :
      
      data = form.cleaned_data
      task = Task.objects.filter(id=data.get('taskid')).first()
      if task :
        new_submission = Submission(
          owner=req.user, 
          code=data.get('code'), 
          lang=data.get('lang'), 
          task=task, 
          status=PENDING_STATUS
        )
        new_submission.save()

        print({
          'SubmissionID': new_submission.id,
          'TaskID': new_submission.task.id,
          'TargLang': new_submission.lang,
          'Code': new_submission.code
        })

        # only normal 1-file tasks - to be improved
        url = f'{API_URL}:{API_SEND_PORT}/submit'
        r = requests.post(url, json={
          'SubmissionID': str(new_submission.id),
          'TaskID': str(new_submission.task.id),
          'TargLang': str(new_submission.lang),
          'Code': [str(new_submission.code)]
        })

        if re.match(r"^Succcessful submission: [0-9]+\s*$", r.text) is not None :
          raise Exception("The submission is not successfully submitted to grader")

        return redirect('core-submission', id=new_submission.id)
  else :
    form = SubmissionForm()

  return render(req, 'core/submit.html', {
    'form' : form
  })