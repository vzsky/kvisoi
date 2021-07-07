from django.db import models
from django.contrib.auth.models import User
from grader_web.settings import verdictSymbol

class Task(models.Model):
  id = models.CharField(max_length=128, primary_key=True, unique=True)
  title = models.CharField(max_length=128)
  author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

  def __str__ (self):
    return self.title

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
    for group in self.groupresult_set.all() :
      res += f'[{group}]'
    return res

class GroupResult (models.Model):
  submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
  score = models.PositiveIntegerField(default=0)
  fullScore = models.PositiveIntegerField(default=0)

  def __str__ (self):
    res = ""
    for case in self.caseresult_set.all() :
      res += str(case)
    return res

class CaseResult (models.Model) :
  group = models.ForeignKey(GroupResult, on_delete=models.CASCADE)
  id = models.PositiveIntegerField(primary_key=True, unique=True)
  verdict = models.CharField(max_length=128)
  message = models.CharField(max_length=128)
  timeUsed = models.PositiveIntegerField(default=0)
  memoryUsed = models.PositiveIntegerField(default=0)
  score = models.PositiveIntegerField(default=0)

  def __str__ (self):
    return verdictSymbol[self.verdict]