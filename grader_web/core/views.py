from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, Submission
from .forms import SubmissionForm, TaskSubmitForm
from django.contrib.auth.decorators import login_required
from grader_web.settings import PENDING_STATUS, API_URL, API_SEND_PORT, supportedLangs
import requests, re
from .tables import SubmissionTable, TaskTable

def home (req) :
  return render(req, 'core/home.html')

# should do pagination (done?)
def tasks (req) : 
  return render(req, 'core/tasks.html', {
    'table' : TaskTable(Task.objects.all())
  })

def task (req, id) :
  return render(req, 'core/task.html', {
    'task' : Task.objects.get(id=id)
  })

# should do pagination (done?)
def submissions (req) :
  return render(req, 'core/submissions.html', {
    'table' : SubmissionTable(Submission.objects.all())
  })

def submission (req, id) : 
  sub = Submission.objects.get(id=id)
  return render(req, 'core/submission.html', {
    'submission' : sub,
  })

def makeSubmission (user, task, data) :
  new_submission = Submission(
    owner=user, 
    code=data.get('code'), 
    lang=data.get('lang'), 
    task=task, 
    status=PENDING_STATUS
  )
  new_submission.save()

  # only normal 1-file tasks
  targlang = supportedLangs[new_submission.lang]['grader']
  url = f'{API_URL}:{API_SEND_PORT}/submit'
  r = requests.post(url, json={
    'SubmissionID': str(new_submission.id),
    'TaskID': str(new_submission.task.id),
    'TargLang': targlang,
    'Code': [str(new_submission.code)]
  })

  if re.match(r"^Succcessful submission: [0-9]+\s*$", r.text) is not None :
    raise Exception("The submission is not successfully submitted to grader")

  return new_submission.id

@login_required
def submit (req) :
  if req.method == 'POST' :
    form = SubmissionForm(req.POST)
    if form.is_valid() :
      data = form.cleaned_data
      task = Task.objects.filter(id=data.get('taskid')).first()
      if task :
        new_submission_id = makeSubmission(req.user, task, data)
        return redirect('core-submission', id=new_submission_id)
  else :
    form = SubmissionForm()

  return render(req, 'core/submit.html', {
    'form' : form
  })

@login_required
def task_submit (req, taskid) :
  if req.method == 'POST' :
    form = TaskSubmitForm(req.POST)
    if form.is_valid() :
      data = form.cleaned_data
      task = Task.objects.filter(id=taskid).first()
      if task :
        new_submission_id = makeSubmission(req.user, task, data)
        return redirect('core-submission', id=new_submission_id)
  else :
    form = TaskSubmitForm()

  return render(req, 'core/submit.html', {
    'form' : form
  })