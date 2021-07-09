from django.db import models
from django.contrib.auth.models import User
from grader_web.settings import verdictSymbol, MEDIA_URL, MEDIA_PDF
import os
import logging
logger = logging.getLogger("mylogger")

class Task(models.Model):
  id = models.CharField(max_length=128, primary_key=True, unique=True)
  title = models.CharField(max_length=128)
  author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

  def __str__ (self):
    return self.title

  @property
  def mediaPath (self):
    return f"/{MEDIA_URL}{MEDIA_PDF}/{self.id}.pdf"


def getUploadPath(name):
  return os.path.join(MEDIA_PDF, name)

def pdfNamer(instance, filename):
  return getUploadPath(f"{instance.pk}.pdf")

class TaskConfig(models.Model):
  task = models.OneToOneField(Task, on_delete=models.CASCADE, primary_key=True)
  pdf = models.FileField(upload_to=pdfNamer)

class Submission(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE, default="")
  code = models.TextField()
  task = models.ForeignKey(Task, on_delete=models.CASCADE, default="")
  lang = models.CharField(max_length=20)
  status = models.CharField(max_length=20)

  score = models.PositiveIntegerField(default=0)
  timeUsed = models.PositiveIntegerField(default=0)
  memoryUsed = models.PositiveIntegerField(default=0)

  def __str__ (self):
    return f'{self.task}@{self.owner}#{self.id}'

  @property
  def result (self):
    return f'{self.score} ({self.timeUsed} s) ({self.memoryUsed} MB)'

  @property
  def response (self):
    res = ""
    logger.info("request submission response")
    for group in self.groupresult_set.all().order_by('id') :
      res += f'[{group}]'
    return res

class GroupResult (models.Model):
  submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
  score = models.PositiveIntegerField(default=0)
  fullScore = models.PositiveIntegerField(default=0)

  def __str__ (self):
    res = ""
    for case in self.caseresult_set.all().order_by('id') :
      res += str(case)
    return f'{res}'

class CaseResult (models.Model) :
  group = models.ForeignKey(GroupResult, on_delete=models.CASCADE)
  verdict = models.CharField(max_length=128)
  message = models.CharField(max_length=128)
  timeUsed = models.PositiveIntegerField(default=0)
  memoryUsed = models.PositiveIntegerField(default=0)
  score = models.PositiveIntegerField(default=0)

  def __str__ (self):
    return verdictSymbol[self.verdict]
